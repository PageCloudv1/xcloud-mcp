# 🧠 Integração com Gemini no xCloud MCP Server

Este documento detalha a integração do xCloud MCP Server com a API do Google Gemini, que fornece a capacidade de análise e automação inteligente.

---

## Visão Geral

O MCP Server utiliza a API Gemini para executar tarefas complexas que exigem compreensão de linguagem natural, como análise de código, categorização de issues e sugestão de melhorias em repositórios.

A integração é projetada para ser modular, permitindo que novas ferramentas e análises sejam adicionadas facilmente.

## Ferramenta Principal: `run_gemini_analysis`

A principal interface com a IA é a ferramenta `run_gemini_analysis` disponível no `server.py`.

```python
@app.tool()
async def run_gemini_analysis(prompt: str, context: Dict = None) -> Dict:
    """
    Executa análise usando Gemini CLI (integração com ferramentas existentes)
    
    Args:
        prompt: Prompt para análise
        context: Contexto adicional
    """
```

Esta função atua como um wrapper genérico, permitindo que qualquer outra parte do sistema (ou um cliente externo) envie um prompt diretamente para a IA e receba uma resposta.

## Configuração

Para que a integração funcione, a seguinte variável de ambiente **deve** ser configurada no arquivo `.env`:

```
# .env

# Chave de API para o Google Gemini
GEMINI_API_KEY="your_gemini_api_key_here"
```

Sem esta chave, qualquer chamada para as ferramentas de análise falhará.

## Como Escrever Prompts Eficazes

A qualidade da resposta da IA depende diretamente da qualidade do prompt. Siga estas diretrizes ao criar novos prompts:

1.  **Seja Específico:** Em vez de "Analise o código", use "Analise este trecho de código Python em busca de possíveis bugs de `asyncio` e sugira otimizações."
2.  **Forneça Contexto:** Inclua informações relevantes no prompt, como o nome do repositório, o título de um issue ou o corpo de um pull request.
3.  **Peça Saídas Estruturadas:** Para facilitar o processamento da resposta, instrua a IA a retornar a saída em um formato específico, como JSON.

    **Exemplo de bom prompt:**
    ```
    Analise o seguinte issue do GitHub e retorne um objeto JSON com as chaves "type", "priority" e "labels".

    Título: ${issue.title}
    Corpo: ${issue.body}
    ```

## Próximos Passos e Melhorias

A integração atual é a base para funcionalidades mais avançadas. Ideias para o futuro incluem:

- **Análise de Pull Requests:** Criar uma ferramenta que recebe o `diff` de um PR e sugere melhorias no código ou aponta possíveis problemas.
- **Geração de Documentação:** Gerar automaticamente a documentação para novas funções ou módulos.
- **Análise de Segurança:** Integrar com ferramentas de segurança e usar a IA para interpretar os resultados e criar issues acionáveis.
- **Otimização de Workflows:** Analisar arquivos de workflow do GitHub Actions e sugerir otimizações de performance e custo.
