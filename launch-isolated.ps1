# Launcher para workspace isolado xCloud MCP
# Execute como: .\launch-isolated.ps1

Write-Host "🚀 Abrindo xCloud MCP em workspace isolado..." -ForegroundColor Cyan

# Abrir VS Code com perfil isolado
& code --profile xcloud-mcp-isolated xcloud-mcp.code-workspace

Write-Host "✅ Workspace isolado aberto!" -ForegroundColor Green
Write-Host "📝 Este workspace não herda suas configurações pessoais" -ForegroundColor Gray
