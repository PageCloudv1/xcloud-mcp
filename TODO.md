# TODO: xCloud MCP Server Development Plan

Este documento descreve as tarefas necessárias para configurar, containerizar e implantar o `xCloud MCP Server` como um serviço independente.

---

### Fase 1: Configuração e Estrutura do Projeto

O objetivo desta fase é estabelecer uma base de código limpa e independente para o servidor.

- [ ] **Inicializar Repositório Git:**
  - [ ] Executar `git init` para criar um novo repositório local.
  - [ ] Criar um repositório remoto no GitHub e conectar os dois.

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

- [ ] **Criar um Serviço `systemd`:**
  - [ ] Escrever um arquivo de serviço (ex: `xcloud-mcp.service`) para gerenciar o ciclo de vida do contêiner.
  - [ ] Configurar o serviço para iniciar o contêiner na inicialização do servidor (`WantedBy=multi-user.target`).
  - [ ] Adicionar uma política de reinicialização (`Restart=always`) para garantir que o serviço se recupere de falhas.

- [ ] **Configurar Nginx como Reverse Proxy:**
  - [ ] Criar um arquivo de configuração do Nginx para o serviço.
  - [ ] Configurar o Nginx para receber tráfego na porta 80 e encaminhá-lo para a porta do contêiner (ex: `localhost:8080`).
  - [ ] **(Opcional, mas recomendado)** Configurar SSL com Let's Encrypt para habilitar HTTPS.

- [ ] **Escrever um Script de Deploy (`deploy.sh`):**
  - [ ] Criar um script que automatize o processo de deploy no servidor.
  - [ ] O script deve:
    1.  Fazer `git pull` das últimas alterações.
    2.  Parar o contêiner antigo.
    3.  Remover a imagem antiga.
    4.  Construir a nova imagem do contêiner (`podman build`).
    5.  Reiniciar o serviço `systemd` para iniciar o novo contêiner.

---

### Fase 4: Testes e Validação

O objetivo é garantir a qualidade e a confiabilidade do serviço.

- [ ] **Configurar Framework de Testes:**
  - [ ] Adicionar `pytest` e `pytest-asyncio` ao `requirements.txt`.
  - [ ] Escrever testes unitários para as ferramentas (`tools`) definidas no `server.py`.
  - [ ] Escrever testes de integração que simulem chamadas de API para os endpoints.

- [ ] **Integrar Testes no CI/CD:**
  - [ ] Criar um workflow de GitHub Actions (`.github/workflows/ci.yml`) no novo repositório.
  - [ ] O workflow deve executar os testes automaticamente em cada `push` ou `pull request`.
