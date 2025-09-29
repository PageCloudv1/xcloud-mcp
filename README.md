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

- [Podman](https://podman.io/getting-started/installation)
- [podman-compose](https://github.com/containers/podman-compose)
- [VS Code](https://code.visualstudio.com/) (recommended)

### Setup

1. **Clone and setup:**
   ```bash
   git clone https://github.com/PageCloudv1/xcloud-mcp.git
   cd xcloud-mcp
   ```

2. **Create environment file:**
   ```bash
   cp .env.example .env
   # Edit .env with your GitHub token
   ```

3. **Start development environment:**
   ```bash
   # Using VS Code (recommended)
   code xcloud-mcp.code-workspace

   # Or using command line
   podman-compose up --build
   ```

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

```
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
