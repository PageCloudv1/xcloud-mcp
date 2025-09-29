# 🔧 Configuração do Gemini para xCloud MCP

Este diretório contém as configurações específicas para integração com o Google Gemini AI.

## Configuração do MCP Server

O arquivo `settings.json` configura o xCloud MCP Server para uso com clientes MCP compatíveis com Gemini.

### Estrutura do Arquivo

```json
{
  "mcpServers": {
    "xcloud-mcp": {
      "command": "podman",
      "args": [
        "run",
        "--rm",
        "-i",
        "--env-file",
        "C:\\Users\\Usuario\\Documents\\PageCloud\\PageCloudv1-repos\\xcloud-mcp\\.env",
        "localhost/xcloud-mcp_xcloud-mcp:latest",
        "fastmcp",
        "run",
        "xcloud_mcp/main.py"
      ]
    }
  }
}
```

## Configuração Passo a Passo

### 1. Verificar Pré-requisitos

```bash
# Verificar se Podman está instalado
podman --version

# Verificar se podman-compose está disponível
podman-compose --version
```

### 2. Configurar Tokens

Edite o arquivo `.env` na raiz do projeto com seus tokens:

```bash
# GitHub Personal Access Token with repo scope
GITHUB_TOKEN=ghp_your_github_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Construir o Container

```bash
# Navegar para o diretório do projeto
cd C:\Users\Usuario\Documents\PageCloud\PageCloudv1-repos\xcloud-mcp

# Construir o container
podman-compose build
```

### 4. Testar Configuração

```bash
# Testar execução manual do MCP server
podman run --rm -i --env-file .env localhost/xcloud-mcp_xcloud-mcp:latest fastmcp run xcloud_mcp/main.py

# Deve aparecer o banner do FastMCP e "Starting MCP server 'xcloud-bot'"
```

## Ferramentas Disponíveis

O xCloud MCP Server fornece 4 ferramentas principais:

1. **`analyze_repository`** - Análise de saúde do repositório
2. **`create_workflow_issue`** - Criação de issues para workflows
3. **`monitor_ci_status`** - Monitoramento de status CI/CD
4. **`get_xcloud_repositories`** - Listagem de repositórios xCloud

## Troubleshooting

### Problema: "command not found: uv"
```bash
# Reinstalar uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc  # ou reiniciar terminal
```

### Problema: "No module named fastmcp"
```bash
# FastMCP é instalado automaticamente com --with
uv run --with fastmcp fastmcp --version
```

### Problema: "Permission denied" ou "Access denied"
```bash
# Verificar permissões do arquivo
ls -la src/xcloud_mcp/main.py

# Usar caminho absoluto completo
uv run --with fastmcp fastmcp run "$(pwd)/src/xcloud_mcp/main.py"
```

### Problema: "GitHub API rate limit"
- Configurar `GITHUB_TOKEN` com um token válido
- O token deve ter permissões de leitura em repositórios

## Logs e Debug

Para debug, execute com variáveis de ambiente:

```bash
export DEBUG=1
export GITHUB_TOKEN=ghp_your_token
uv run --with fastmcp fastmcp run src/xcloud_mcp/main.py
```

## Integração com Clients

Este servidor MCP é compatível com:
- Claude Desktop
- VS Code com extensões MCP
- Outros clientes que suportam o protocolo MCP

---

**Dica**: Mantenha seus tokens seguros e nunca os commite no repositório!
