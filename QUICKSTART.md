# 🚀 Quick Start Guide - xCloud MCP Server

This guide helps you get the xCloud MCP Server up and running quickly.

## ⚡ 5-Minute Setup

### 1. Install Prerequisites

```bash
# Install Python 3.11+
python --version  # Should be 3.11 or higher

# Install uv (Python package installer)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Optional: Install Podman for container deployment
```

### 2. Clone & Configure

```bash
# Clone the repository
git clone https://github.com/PageCloudv1/xcloud-mcp.git
cd xcloud-mcp

# Set environment variables
export GITHUB_TOKEN=ghp_your_github_token_here
export GEMINI_API_KEY=your_gemini_api_key_here  # Optional
```

### 3. Run the Server

**Option A: Direct Run (Recommended for Testing)**
```bash
uv run --with fastmcp --with aiohttp fastmcp run src/xcloud_mcp/main.py
```

**Option B: Container (Recommended for Production)**
```bash
podman-compose up --build
```

### 4. Test the Server

```bash
# Health check
curl http://localhost:8000/health
# Should return: {"status": "ok"}
```

## 🤖 Using with AI Assistants

### GitHub Copilot

1. Configure MCP in your editor
2. Ask Copilot to use the xCloud tools:
   ```
   "Analyze the PageCloudv1/xcloud-bot repository"
   "Create a CI workflow issue for xcloud-mcp"
   "Show CI status for xcloud-docs"
   ```

See [copilot-instructions.md](./copilot-instructions.md) for details.

### Google Gemini

1. Follow setup in [.gemini/README.md](./.gemini/README.md)
2. Configure the MCP server in Gemini settings
3. Use natural language to interact with tools

See [GEMINI.md](./GEMINI.md) for details.

## 🛠️ Available Tools

### 1. `analyze_repository`
Analyze a GitHub repository for improvements.

**Example:**
```
analyze_repository(repo_url="PageCloudv1/xcloud-mcp", analysis_type="general")
```

### 2. `create_workflow_issue`
Create an issue for workflow implementation.

**Example:**
```
create_workflow_issue(repo="PageCloudv1/xcloud-mcp", workflow_type="ci")
```

Workflow types: `ci`, `cd`, `build`, `test`, `deploy`, `main`

### 3. `monitor_ci_status`
Monitor CI/CD pipeline status.

**Example:**
```
monitor_ci_status(repo="PageCloudv1/xcloud-mcp", limit=10)
```

### 4. `get_xcloud_repositories`
List all xCloud ecosystem repositories.

**Example:**
```
get_xcloud_repositories()
```

## 🧪 Running Tests

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src/xcloud_mcp --cov-report=html

# View coverage report
open htmlcov/index.html
```

## 🔍 Quality Checks

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
flake8 src/ tests/

# Run all checks
black --check src/ tests/ && isort --check-only src/ tests/ && flake8 src/ tests/
```

## 📚 Documentation

- **[README.md](./README.md)** - Complete documentation
- **[MCP_INTEGRATION_REVIEW.md](./MCP_INTEGRATION_REVIEW.md)** - Full integration review
- **[copilot-instructions.md](./copilot-instructions.md)** - Copilot usage guide
- **[GEMINI.md](./GEMINI.md)** - Gemini integration guide
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - Contribution guidelines

## ⚙️ Configuration

### Environment Variables

```bash
# Required
GITHUB_TOKEN=ghp_your_token_here

# Optional
GEMINI_API_KEY=your_gemini_key_here
X_CLOUD_MCP_TRANSPORT=http  # or stdio, sse
X_CLOUD_MCP_HOST=0.0.0.0
X_CLOUD_MCP_PORT=8000
```

### GitHub Token Permissions

Required scopes:
- `repo` - Full repository access
- `read:org` - Read organization data
- `workflow` - Update GitHub Actions workflows

## 🐛 Troubleshooting

### Server won't start

```bash
# Check Python version
python --version  # Must be 3.11+

# Verify token is set
echo $GITHUB_TOKEN

# Check for port conflicts
lsof -i :8000
```

### Tests failing

```bash
# Clean environment
rm -rf .venv __pycache__ .pytest_cache

# Reinstall dependencies
pip install -r requirements.txt -r requirements-dev.txt

# Run tests with verbose output
pytest tests/ -vv
```

### Import errors

```bash
# Ensure you're in the project root
pwd  # Should end with /xcloud-mcp

# Add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

## 🚀 Deployment

### Production Checklist

- [ ] Set `GITHUB_TOKEN` securely
- [ ] Configure firewall rules (if exposing HTTP)
- [ ] Set up monitoring/logging
- [ ] Test all MCP tools
- [ ] Review security settings
- [ ] Configure backup/recovery

### Docker/Podman Deployment

```bash
# Build image
podman build -t xcloud-mcp:latest -f Containerfile .

# Run container
podman run -d \
  --name xcloud-mcp \
  -e GITHUB_TOKEN=$GITHUB_TOKEN \
  -p 8000:8000 \
  xcloud-mcp:latest
```

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/PageCloudv1/xcloud-mcp/issues)
- **Documentation:** [xCloud Docs](https://pagecloudv1.github.io/xcloud-docs/)
- **Discussions:** [GitHub Discussions](https://github.com/PageCloudv1/xcloud-mcp/discussions)

## ✅ Quick Health Check

Run this to verify everything is working:

```bash
# 1. Start server
uv run --with fastmcp --with aiohttp fastmcp run src/xcloud_mcp/main.py &

# 2. Wait a moment
sleep 5

# 3. Test health endpoint
curl http://localhost:8000/health

# 4. Run tests
pytest tests/ -v

# 5. Stop server
kill %1
```

Expected results:
- Health check returns `{"status": "ok"}`
- All tests pass (18/18)

---

**Status:** ✅ Ready for use  
**Version:** 0.1.0  
**Last Updated:** October 1, 2025
