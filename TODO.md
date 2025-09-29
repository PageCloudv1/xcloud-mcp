# TODO: xCloud MCP Server Development Plan

Este documento descreve as tarefas necessárias para configurar, containerizar e implantar o `xCloud MCP Server` como um serviço independente.

---

### Fase 1: Configuração e Estrutura do Projeto

O objetivo desta fase é estabelecer uma base de código limpa e independente para o servidor.

- [x] **Inicializar Repositório Git:**
  - [x] Executar `git init` para criar um novo repositório local.
  - [x] Criar um repositório remoto no GitHub e conectar os dois.

- [x] **Criar `.gitignore`:**
  - [x] Adicionar entradas para ignorar arquivos e diretórios específicos do Python, como `venv/`, `__pycache__/`, `*.pyc`, e o arquivo `.env`.

- [x] **Criar `README.md`:**
  - [x] Documentar o propósito do `xCloud MCP Server`.
  - [x] Adicionar instruções claras sobre como configurar o ambiente de desenvolvimento local (`venv`).
  - [x] Listar todas as variáveis de ambiente necessárias (criar um `.env.example`).

- [x] **Adicionar um Endpoint de Health Check:**
  - [x] Implementar um endpoint simples como `/health` no `server.py` que retorne um status `200 OK` para monitoramento.

---

### Fase 2: Containerização com Podman

O objetivo é criar uma imagem de contêiner leve e segura para o servidor.

- [x] **Criar `Containerfile`:**
  - [x] Usar uma imagem base `python:3.11-slim`.
  - [x] Implementar a cópia de `requirements.txt` e a instalação de dependências em uma camada separada para otimizar o cache de build.
  - [x] Copiar o código da aplicação.
  - [x] Expor a porta `8000` e definir o `CMD` para iniciar o servidor.

- [x] **Criar `.containerignore`:**
  - [x] Adicionar `venv`, `__pycache__`, `.git`, `.gitignore` e `README.md` para manter a imagem final o menor possível.

- [x] **Criar `podman-compose.yml`:**
  - [x] Definir um serviço `mcp-server`.
  - [x] Mapear a porta do host (ex: `8080`) para a porta do contêiner (`8000`).
  - [x] Configurar o carregamento de variáveis de ambiente a partir de um arquivo `.env` para facilitar o desenvolvimento local.

---

### Fase 3: Implantação e Automação (Deploy)

O objetivo é implantar o contêiner no servidor de produção e garantir que ele rode de forma confiável.

- [x] **Criar um Serviço `systemd`:**
  - [x] Escrever um arquivo de serviço (ex: `xcloud-mcp.service`) para gerenciar o ciclo de vida do contêiner.
  - [x] Configurar o serviço para iniciar o contêiner na inicialização do servidor (`WantedBy=multi-user.target`).
  - [x] Adicionar uma política de reinicialização (`Restart=always`) para garantir que o serviço se recupere de falhas.

- [x] **Configurar Nginx como Reverse Proxy:**
  - [x] Criar um arquivo de configuração do Nginx para o serviço.
  - [x] Configurar o Nginx para receber tráfego na porta 80 e encaminhá-lo para a porta do contêiner (ex: `localhost:8080`).
  - [x] **(Opcional, mas recomendado)** Configurar SSL com Let's Encrypt para habilitar HTTPS.

- [x] **Criar um Workflow de Deploy (`deploy.yml`):**
  - [x] Criar um workflow que automatize o processo de deploy no servidor.
  - [x] O workflow deve:
    1.  Ser acionado após a publicação de uma nova imagem.
    2.  Acessar o servidor via SSH.
    3.  Fazer `git pull` das últimas alterações.
    4.  Reiniciar o serviço `systemd` para iniciar o novo contêiner.

---

### Fase 4: Testes e Validação

O objetivo é garantir a qualidade e a confiabilidade do serviço.

- [x] **Configurar Framework de Testes:**
  - [x] Adicionar `pytest`, `pytest-asyncio` e `pytest-mock` ao `requirements-dev.txt`.
  - [x] Escrever testes unitários para as ferramentas (`tools`) definidas no `server.py`.
  - [x] Escrever testes de integração que simulem chamadas de API para os endpoints.

- [x] **Integrar Testes no CI/CD:**
  - [x] Criar um workflow de GitHub Actions (`.github/workflows/ci.yml`) no novo repositório.
  - [x] O workflow deve executar os testes automaticamente em cada `push` ou `pull request`.
  - [x] Criar um workflow (`.github/workflows/publish.yml`) para publicar a imagem do contêiner no GHCR em cada `release`.
