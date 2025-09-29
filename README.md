# 🤖 xCloud MCP Server

[![Tests](https://img.shields.io/badge/tests-19%2F19%20passing-brightgreen)](./tests/)
[![Coverage](https://img.shields.io/badge/coverage-91%25-brightgreen)](./COVERAGE_REPORT.md)
[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

A high-performance **Model Context Protocol (MCP) Server** built with FastMCP, providing AI agents and automation tools with powerful GitHub integration and DevOps automation capabilities.

## ✨ Features

- � **4 MCP Tools** for GitHub automation
- 🧪 **91% Test Coverage** with comprehensive test suite
- 🐳 **Containerized Development** with Podman
- 🔍 **Real-time Debugging** support
- 📊 **Coverage Reporting** with HTML output
- ⚡ **Hot Reload** development environment

## 🛠️ MCP Tools Available

| Tool | Description | Status |
|------|-------------|---------|
| `create_workflow_issue` | Create GitHub issues for workflow failures | ✅ Tested |
| `monitor_ci_status` | Monitor CI/CD pipeline status | ✅ Tested |
| `get_xcloud_repositories` | List PageCloudv1 repositories with workflows | ✅ Tested |
| `github_api_request` | Low-level GitHub API interaction | ✅ Tested |

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **[uv](https://github.com/astral-sh/uv)** (Python package installer)
- **GitHub Token** with repository access
- **[Podman](https://podman.io/getting-started/installation)** (optional, for containerized development)
- **[VS Code](https://code.visualstudio.com/)** (recommended)

### Setup

1. **Clone and setup:**
   ```bash
   git clone https://github.com/PageCloudv1/xcloud-mcp.git
   cd xcloud-mcp
   ```

2. **Install uv (if not already installed):**

   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows (PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. **Configure environment:**

   ```bash
   # Set environment variables
   export GITHUB_TOKEN=ghp_your_github_token_here
   export GEMINI_API_KEY=your_gemini_api_key_here  # Optional
   ```

### Start MCP Server

#### Option A: Direct MCP Server (Recommended)

```bash
# Run the MCP server using uv and FastMCP
uv run --with fastmcp fastmcp run src/xcloud_mcp/main.py

# Server will be available for MCP clients
```

#### Option B: Development Environment (with debugging)

```bash
# Using VS Code (recommended)
code xcloud-mcp.code-workspace

# Or using command line
podman-compose up --build
```

## 🔧 MCP Client Configuration

The xCloud MCP Server can be configured in multiple ways depending on your client and requirements.

### Option A: Container-based (Recommended)

This is the most reliable approach as it includes all dependencies:

```json
{
  "xcloud-mcp": {
    "command": "podman",
    "args": [
      "run",
      "--rm",
      "-i",
      "--env-file",
      "/absolute/path/to/xcloud-mcp/.env",
      "localhost/xcloud-mcp_xcloud-mcp:latest",
      "fastmcp",
      "run",
      "xcloud_mcp/main.py"
    ]
  }
}
```

### Option B: Direct uv execution

For development or when containers aren't preferred:

```json
{
  "xcloud-mcp": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "fastmcp",
      "fastmcp",
      "run",
      "/absolute/path/to/xcloud-mcp/src/xcloud_mcp/main.py"
    ],
    "env": {
      "GITHUB_TOKEN": "ghp_your_token_here",
      "GEMINI_API_KEY": "your_gemini_key_here"
    }
  }
}
```

### Setup Steps

1. **Prepare container** (for Option A):

   ```bash
   cd /path/to/xcloud-mcp
   podman-compose build
   ```

2. **Configure environment**:

   ```bash
   # Edit .env file with your tokens
   GITHUB_TOKEN=ghp_your_github_token_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Test configuration**:

   ```bash
   # Test container approach
   podman run --rm -i --env-file .env localhost/xcloud-mcp_xcloud-mcp:latest fastmcp run xcloud_mcp/main.py

   # Should show FastMCP banner and "Starting MCP server 'xcloud-bot'"
   ```

### Client-Specific Configurations

#### Claude Desktop

Add to your `settings.json`:

```json
{
  "mcpServers": {
    "xcloud-mcp": {
      "command": "podman",
      "args": ["run", "--rm", "-i", "--env-file", "/path/to/.env", "localhost/xcloud-mcp_xcloud-mcp:latest", "fastmcp", "run", "xcloud_mcp/main.py"]
    }
  }
}
```

#### VS Code with MCP Extension

Configure in your workspace or user settings with the appropriate command from Options A or B above.

#### GitHub Copilot Integration

The GitHub Copilot integration works differently from other MCP clients. Instead of connecting directly to the MCP server, Copilot uses the server's tools through intelligent orchestration.

**How it works:**

1. **Copilot Instructions**: Located in [`.github/copilot-instructions.md`](.github/copilot-instructions.md)
2. **Tool Orchestration**: Copilot translates natural language requests into MCP tool calls
3. **No Direct Connection**: Copilot doesn't connect to the MCP server directly

**Setup for Copilot:**

1. **Ensure MCP server is running** (using any of the options above)
2. **Copilot automatically detects** the instructions in `.github/copilot-instructions.md`
3. **Use natural language** to interact with xCloud tools through Copilot

**Example Copilot commands:**

```text
"Analyze the xcloud-bot repository and tell me what can be improved"
"Create a CI workflow issue for the xcloud-mcp repository"
"Show me the last 10 builds for PageCloudv1/xcloud-docs"
"List all xCloud repositories that don't have workflows"
```

**Available Tools via Copilot:**

- `analyze_repository` - Repository health analysis
- `create_workflow_issue` - Automated issue creation for workflows
- `monitor_ci_status` - CI/CD pipeline monitoring
- `get_xcloud_repositories` - xCloud ecosystem repository listing

**Note**: The MCP server must be running locally for Copilot to access the tools.

### 🧠 Making Copilot Smarter

You can enhance Copilot's capabilities by setting up custom instructions, customizing the development environment, and configuring Model Context Protocol (MCP) servers.

#### Custom Instructions Setup

1. **Repository-Level Instructions**:
   - The `.github/copilot-instructions.md` file provides project-specific guidance to Copilot
   - Copilot automatically detects and uses these instructions when working in this repository
   - Instructions define the xCloud MCP server's role and available tools

2. **Personal Copilot Configuration**:

   ```bash
   # In VS Code, access Copilot settings:
   # 1. Open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
   # 2. Search "Copilot: Open Settings"
   # 3. Configure your preferences
   ```

3. **Workspace-Specific Settings**:

   ```json
   // In .vscode/settings.json
   {
     "github.copilot.enable": {
       "*": true,
       "yaml": true,
       "plaintext": false
     },
     "github.copilot.editor.enableAutoCompletions": true
   }
   ```

#### MCP Server Configuration for Copilot

1. **Enable MCP Integration**:

   ```bash
   # Ensure your MCP server is running
   uv run --with fastmcp fastmcp run src/xcloud_mcp/main.py

   # Or with container
   podman run --rm -i --env-file .env localhost/xcloud-mcp_xcloud-mcp:latest fastmcp run xcloud_mcp/main.py
   ```

2. **VS Code MCP Extension** (if available):

   ```bash
   # Install MCP extension for VS Code
   code --install-extension mcp-extension-id
   ```

3. **Configure MCP in VS Code settings**:

   ```json
   // In settings.json
   {
     "mcp.servers": {
       "xcloud-mcp": {
         "command": "podman",
         "args": ["run", "--rm", "-i", "--env-file", ".env", "localhost/xcloud-mcp_xcloud-mcp:latest", "fastmcp", "run", "xcloud_mcp/main.py"]
       }
     }
   }
   ```

#### Development Environment Customization

1. **Workspace Configuration**:

   ```bash
   # Open the xCloud MCP workspace
   code xcloud-mcp.code-workspace
   ```

2. **Environment Variables**:

   ```bash
   # Ensure tokens are configured
   export GITHUB_TOKEN=ghp_your_token_here
   export GEMINI_API_KEY=your_gemini_key_here
   ```

3. **Debugging Setup**:

   ```json
   // In .vscode/launch.json (already configured)
   {
     "name": "Attach to MCP Server",
     "type": "python",
     "request": "attach",
     "connect": {
       "host": "localhost",
       "port": 5678
     }
   }
   ```

#### Best Practices for Copilot + MCP

1. **Use Natural Language**: Ask Copilot questions in plain English about repository analysis, CI/CD status, or workflow management

2. **Leverage Context**: Copilot understands the project structure and can suggest relevant xCloud operations

3. **Combine Tools**: Ask for complex operations that use multiple MCP tools together

4. **Iterate**: Use Copilot's suggestions to refine your automation workflows

**Learn More**:

- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [VS Code Copilot Tips](https://code.visualstudio.com/docs/copilot/overview)
- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/)

#### Gemini Integration

See detailed configuration in [`.gemini/README.md`](.gemini/README.md) for Gemini-specific setup.

### GitHub & Environment Configuration

The server requires specific configurations:

- **`.env`**: Contains GitHub and Gemini API tokens (never commit this file)
- **`.github/`**: Contains GitHub workflows and Copilot instructions
- **`GEMINI.md`**: Configuration and usage guide for Gemini API integration
- **Environment variables**: Required tokens and API keys for authentication

## 🧪 Testing

The project has a comprehensive test suite with **91% coverage**:

### Run Tests

```bash
# Using VS Code Task
Ctrl+Shift+P → "Tasks: Run Task" → "Run Tests"

# Using command line
podman-compose -f podman-compose.test.yml up --build --abort-on-container-exit
```

### Generate Coverage Report

```bash
# Coverage report is automatically generated
open htmlcov/index.html  # View detailed HTML report
```

### Test Statistics

- **19 total tests** - All passing ✅
- **4 MCP tools** - Fully tested
- **Coverage areas**: Success scenarios, error handling, edge cases

## 🐳 Development

### Development Server

```bash
podman-compose up --build
# Server runs on http://localhost:8000
# Debugger available on port 5678
```

### Debug in VS Code

1. Start dev container: `Compose Up (Dev)` task
2. Attach debugger: `Python: Attach to App`
3. Set breakpoints and debug

### Available Commands

```bash
# Start services
podman-compose up --build

# Run tests
podman-compose -f podman-compose.test.yml up --build --abort-on-container-exit

# Stop services
podman-compose down

# View logs
podman-compose logs -f

# Run linting
podman-compose exec xcloud-mcp python -m flake8 src tests
```

## 📁 Project Structure

```text
xcloud-mcp/
├── .github/                     # GitHub workflows and configuration
│   ├── profile/
│   └── workflows/
├── .vscode/                     # VS Code settings and tasks
├── deploy/                      # Deployment configurations
│   ├── nginx.conf              # Nginx configuration
│   └── xcloud-mcp.service      # Systemd service
├── src/                        # Source code
│   └── xcloud_mcp/             # Main application package
│       ├── __init__.py
│       └── main.py             # MCP server implementation
├── tests/                      # Test suite (91% coverage)
│   ├── test_server.py          # Server functionality tests
│   └── test_tools.py           # MCP tools comprehensive tests
├── CHANGELOG.md                # Version history
├── CODE_OF_CONDUCT.md          # Community guidelines
├── Containerfile              # Container definition
├── CONTRIBUTING.md             # Contribution guidelines
├── COVERAGE_REPORT.md          # Detailed test coverage report
├── LICENSE                     # MIT License
├── podman-compose.yml          # Development orchestration
├── podman-compose.test.yml     # Test environment
├── podman-compose.debug-test.yml # Debug test environment
├── pytest.ini                 # Test configuration
├── README.md                   # This file
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
├── setup-git-config.ps1       # Git configuration script
├── setup-workspace.ps1         # Workspace setup script
├── TODO.md                     # Project tasks and roadmap
└── xcloud-mcp.code-workspace   # VS Code workspace configuration
```

## 🔧 Configuration

### Environment Variables

```env
GITHUB_TOKEN=ghp_your_github_token_here
GEMINI_API_KEY=your_gemini_api_key_here  # Optional
```

### VS Code Integration

- **Workspace**: `xcloud-mcp.code-workspace`
- **Tasks**: Build, test, debug, lint
- **Debugging**: Attach to container
- **Extensions**: Python, Docker, MCP support

## 📊 Code Quality

- **Test Coverage**: 91% (90/98 lines covered)
- **Linting**: flake8 compliant
- **Type Hints**: Throughout codebase
- **Documentation**: Comprehensive docstrings
- **Error Handling**: Robust exception management

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Run tests: `podman-compose -f podman-compose.test.yml up`
4. Ensure 80%+ coverage maintained
5. Commit changes: `git commit -m 'Add amazing feature'`
6. Push branch: `git push origin feature/amazing-feature`
7. Open Pull Request

## � Available Tasks (VS Code)

- `Compose Up (Dev)` - Start development server
- `Compose Down` - Stop all services
- `Run Tests` - Execute test suite
- `Debug Tests` - Debug test execution
- `View Logs` - Show container logs
- `Lint Python Code` - Run code linting
- `Format Python Code` - Auto-format code

## 🔍 Monitoring & Debugging

- **Health Check**: `GET /health`
- **Debug Port**: 5678 (debugpy)
- **Logs**: Real-time via `podman-compose logs -f`
- **Test Reports**: HTML coverage in `htmlcov/`

## 📈 Performance

- **Container-based**: Isolated and reproducible
- **Hot Reload**: Instant code changes
- **Efficient Testing**: Parallel execution
- **Resource Optimized**: Minimal container footprint

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built with ❤️ by PageCloudv1 Team
