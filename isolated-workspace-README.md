# 🔒 Workspace Isolado - xCloud MCP

Este workspace foi configurado para ser **completamente isolado** das suas configurações pessoais do VS Code, evitando conflitos e mantendo um ambiente limpo e específico para o projeto.

## 🚀 Como Usar o Workspace Isolado

### Configuração Inicial (Execute UMA vez)
```powershell
# 1. Configurar workspace isolado
.\setup-isolated-workspace.ps1

# 2. Configurar Git específico do projeto
.\setup-git-config.ps1 -UserName "Seu Nome" -UserEmail "seu.email@exemplo.com"
```

### Abrir o Workspace Isolado
```powershell
# Opção 1: Script launcher (recomendado)
.\launch-isolated.ps1

# Opção 2: Comando direto
code --profile xcloud-mcp-isolated xcloud-mcp.code-workspace
```

## 🔒 O que é Isolado

### ✅ Configurações Isoladas
- **Settings**: Configurações específicas do projeto
- **Extensions**: Apenas extensões essenciais
- **Keybindings**: Atalhos limpos, sem conflitos
- **Git**: Configurações específicas do repositório
- **GitHub**: Sem herdar configurações pessoais
- **Themes**: Tema padrão, sem personalizações

### ❌ Não Herdado das Configurações Pessoais
- Extensões pessoais instaladas
- Configurações globais do Git
- Temas e personalizações
- Snippets personalizados
- Configurações do GitHub Copilot pessoais
- Configurações de terminal personalizadas

## 📁 Estrutura do Perfil Isolado

```
%APPDATA%\Code\User\profiles\xcloud-mcp-isolated\
├── settings.json     # Configurações específicas
├── keybindings.json  # Atalhos limpos
└── extensions/       # Apenas extensões essenciais
```

## 🔧 Extensões Instaladas (Mínimas)

### Essenciais para Python
- `ms-python.python` - Suporte Python
- `ms-python.black-formatter` - Formatação Black
- `ms-python.isort` - Organização de imports
- `ms-python.flake8` - Linting
- `ms-python.debugpy` - Debug Python

### Suporte de Arquivos
- `ms-vscode.vscode-json` - JSON
- `redhat.vscode-yaml` - YAML
- `ms-vscode.vscode-docker` - Docker/Podman

## 🐛 Debug no Workspace Isolado

### Configurações de Debug Disponíveis
1. **Python: Attach to App Container** - Anexar ao container principal
2. **Python: Attach to Test Container** - Anexar ao container de testes
3. **Python: Local Debug** - Debug local sem containers

### Como Debugar
1. Execute a task `Compose Up (Dev)`
2. Use `F5` para iniciar debug
3. Escolha a configuração apropriada

## ⚙️ Tasks Disponíveis

### Desenvolvimento
- `Compose Up (Dev)` - Iniciar ambiente (F1 → Tasks: Run Build Task)
- `Compose Down` - Parar serviços
- `View Logs` - Ver logs em tempo real

### Code Quality
- `Lint Python Code` - Verificar código
- `Format Python Code` - Formatear com Black
- `Sort Imports` - Organizar imports
- `Full Code Format` - Formatação completa

### Utilitários
- `Install Dependencies` - Instalar dependências
- `Clean Python Cache` - Limpar cache Python

## 🔄 Atualizando o Workspace Isolado

### Limpar e Recriar
```powershell
.\setup-isolated-workspace.ps1 -Clean
```

### Adicionar Nova Extensão
```powershell
code --profile xcloud-mcp-isolated --install-extension publisher.extension-name
```

## 🚨 Troubleshooting

### Problema: VS Code não abre com perfil isolado
**Solução**: Verifique se o VS Code está atualizado:
```powershell
code --version
```

### Problema: Extensões não carregam
**Solução**: Reinstale as extensões:
```powershell
.\setup-isolated-workspace.ps1 -Clean
```

### Problema: Git não funciona corretamente
**Solução**: Reconfigure o Git:
```powershell
.\setup-git-config.ps1 -UserName "Nome" -UserEmail "email@exemplo.com"
```

### Problema: Debugger não conecta
**Solução**: Verifique se o container está rodando:
```powershell
podman-compose ps
```

## 📝 Personalização Permitida

Você pode personalizar **apenas no contexto deste projeto**:

### Settings Locais (.vscode/settings.json)
```json
{
  "python.defaultInterpreterPath": "seu/caminho/python",
  "terminal.integrated.shell.windows": "seu-shell.exe"
}
```

### Variáveis de Ambiente (.env)
```env
GITHUB_TOKEN=seu_token
GEMINI_API_KEY=sua_chave
```

## 🔐 Segurança

- **Tokens**: Armazenados apenas localmente no projeto
- **Credenciais**: Específicas do repositório
- **Configurações**: Não vazam para outros projetos
- **Extensões**: Conjunto mínimo e controlado

## 📚 Documentação Adicional

- [VS Code Profiles](https://code.visualstudio.com/docs/editor/profiles)
- [Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings)
- [Git Configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
