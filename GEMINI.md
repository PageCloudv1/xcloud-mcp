# 🧠 Integração com Gemini no xCloud MCP Server

Este documento detalha a integração do xCloud MCP Server com a API do Google Gemini, que fornece a capacidade de análise e automação inteligente.

---

## Visão Geral

O MCP Server utiliza a API Gemini como o motor de inteligência para compreender comandos em linguagem natural e executar tarefas complexas e automatizadas relacionadas a repositórios do GitHub.

A integração é projetada em torno de um sistema de **ferramentas (tools)**, onde cada ferramenta é uma função Python específica que o Gemini pode escolher executar para atender a uma solicitação.

## Como Funciona

Em vez de uma única função de "análise genérica", o Gemini atua como um orquestrador. Quando um comando é enviado ao servidor, o Gemini:

1.  **Interpreta** a intenção do usuário.
2.  **Seleciona** a ferramenta mais apropriada para a tarefa (por exemplo, `analyze_repository` ou `create_workflow_issue`).
3.  **Extrai** os parâmetros necessários do comando (como o nome do repositório).
4.  **Executa** a ferramenta com esses parâmetros.

Essa abordagem modular permite adicionar novas capacidades de forma estruturada e confiável.

## Configuração

Para que a integração funcione, a seguinte variável de ambiente **deve** ser configurada no arquivo `.env`:

```
# .env

# Chave de API para o Google Gemini
GEMINI_API_KEY="your_gemini_api_key_here"
```

Sem esta chave, o servidor não conseguirá se autenticar com a API do Gemini e as ferramentas inteligentes falharão.

## Ferramentas Disponíveis

Atualmente, as seguintes ferramentas estão disponíveis para serem usadas pelo Gemini:

-   `analyze_repository`: Analisa um repositório GitHub (workflows, atividade recente) e sugere melhorias.
-   `create_workflow_issue`: Cria uma issue detalhada em um repositório para implementar um tipo específico de workflow (CI, CD, etc.).
-   `monitor_ci_status`: Monitora o status das execuções de workflows em um repositório.
-   `get_xcloud_repositories`: Lista todos os repositórios da organização `PageCloudv1` que estão relacionados ao xCloud.

## Como Escrever Comandos Eficazes

A qualidade da automação depende da clareza do seu comando. Siga estas diretrizes:

1.  **Seja Direto e Específico:** Em vez de um prompt vago, dê um comando claro.
    *   **Ruim:** "Acho que precisamos de CI."
    *   **Bom:** "Crie uma issue para implementar um workflow de CI no repositório `PageCloudv1/xcloud-bot`."

2.  **Use o Nome das Ferramentas (Opcional):** Você pode até mesmo sugerir a ferramenta no seu comando para ser mais explícito.
    *   **Exemplo:** "Use a ferramenta `analyze_repository` para `PageCloudv1/xcloud-mcp`."

3.  **Forneça Todos os Dados Necessários:** Certifique-se de que o comando contém os parâmetros que a ferramenta precisa, como o nome completo do repositório (`owner/repo`).

## Próximos Passos e Melhorias

A integração atual é a base para funcionalidades mais avançadas. Ideias para o futuro incluem:

-   **Análise de Pull Requests:** Criar uma ferramenta que recebe o `diff` de um PR e sugere melhorias no código.
-   **Geração de Documentação:** Gerar automaticamente a documentação para novas funções ou módulos.
-   **Análise de Segurança:** Integrar com ferramentas de segurança e usar a IA para interpretar os resultados e criar issues acionáveis.
-   **Otimização de Workflows:** Analisar arquivos de workflow do GitHub Actions e sugerir otimizações de performance e custo.
