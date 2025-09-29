# TODO: xCloud MCP Server Testing Plan

Este documento descreve as tarefas para testar e validar o `xCloud MCP Server` após a reestruturação do projeto.

---

### Fase 1: Testes Locais

O objetivo é garantir que a aplicação funcione corretamente no ambiente de desenvolvimento local.

- [x] **Validar Build Local:**
  - [x] Executar `podman-compose up --build` para construir a imagem do contêiner.
  - [x] Verificar se a imagem é construída sem erros e se o contêiner inicia.

- [ ] **Executar Testes Automatizados:**
  - [ ] Usar `podman-compose -f podman-compose.test.yml up --build` para rodar a suíte de testes.
  - [ ] Confirmar que todos os testes (`pytest`) passam com sucesso.

- [ ] **Testar Ferramentas Manualmente:**
  - [ ] Iniciar o servidor em modo de desenvolvimento.
  - [ ] Fazer chamadas para cada uma das ferramentas (`@app.tool`) para garantir que elas respondem como esperado após a refatoração.
    - [ ] `analyze_repository`
    - [ ] `create_workflow_issue`
    - [ ] `monitor_ci_status`
    - [ ] `get_xcloud_repositories`

---

### Fase 2: Validação do Pipeline de CI/CD

O objetivo é garantir que os workflows de automação estão funcionando corretamente.

- [ ] **Testar Workflow de CI:**
  - [ ] Fazer um `push` para uma branch de teste.
  - [ ] Verificar se o workflow `CI - Run Tests` é acionado no GitHub Actions.
  - [ ] Confirmar que todos os jobs do workflow são concluídos com sucesso.

- [ ] **Testar Workflow de Publicação:**
  - [ ] Criar uma `release` de teste no GitHub.
  - [ ] Verificar se o workflow `Publish Container Image` é acionado.
  - [ ] Confirmar que a imagem do contêiner é publicada com sucesso no GitHub Container Registry (GHCR).

- [ ] **Testar Workflow de Deploy:**
  - [ ] Verificar se o workflow `CD - Deploy to Production` é acionado automaticamente após a conclusão do workflow de publicação.
  - [ ] Confirmar que o deploy no servidor de produção é executado sem erros.

---

### Fase 3: Verificação Pós-Deploy

O objetivo é validar a aplicação em produção após o deploy.

- [ ] **Verificar Health Check:**
  - [ ] Acessar o endpoint `/health` no domínio de produção.
  - [ ] Confirmar que o serviço responde com `{"status": "ok"}`.

- [ ] **Teste de Sanidade em Produção:**
  - [ ] Executar um teste rápido em uma das ferramentas (ex: `get_xcloud_repositories`) no ambiente de produção para garantir que a lógica principal está funcionando.
