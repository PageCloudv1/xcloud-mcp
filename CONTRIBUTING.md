# Guia de Contribuição para o xCloud MCP Server

Agradecemos o seu interesse em contribuir! Este guia fornecerá tudo o que você precisa para começar a desenvolver e adicionar novas funcionalidades ao servidor.

## Filosofia

O xCloud MCP Server atua como um **orquestrador inteligente**. O objetivo não é criar uma aplicação monolítica, mas sim um conjunto de **ferramentas (tools)** independentes e bem definidas que o modelo de IA (Gemini) pode usar para realizar tarefas complexas.

Cada ferramenta deve ser vista como um bloco de construção atômico e reutilizável.

## Adicionando Novas Ferramentas

Esta é a principal forma de contribuição. Adicionar uma nova ferramenta permite que o MCP Server execute novas tarefas. O processo é simples e direto.

### 1. Estrutura da Função

Toda ferramenta é uma função Python `async` que recebe parâmetros específicos e retorna um dicionário.

```python
import logging
from fastmcp import app  # Import a instância `app` do main

@app.tool()
async def nome_da_ferramenta(parametro1: str, parametro2: int = 0) -> dict:
    """
    Descrição clara e concisa do que a ferramenta faz. 
    Esta descrição é crucial, pois o Gemini a utiliza para decidir quando usar a ferramenta.

    Args:
        parametro1: Descrição do primeiro parâmetro.
        parametro2: Descrição do segundo parâmetro, com valor padrão.
    """
    logging.info(f"Executando nome_da_ferramenta com: {parametro1}, {parametro2}")
    
    try:
        # --- Lógica da Ferramenta ---
        # (Ex: Chamar uma API, executar um comando, etc.)
        
        resultado = f"Operação bem-sucedida com {parametro1}"
        
        logging.info("Execução da ferramenta concluída com sucesso.")
        return {"status": "sucesso", "resultado": resultado}

    except Exception as e:
        logging.error(f"Erro ao executar nome_da_ferramenta: {str(e)}")
        return {
            "error": {
                "type": "TOOL_EXECUTION_ERROR",
                "message": f"Falha na execução da ferramenta: {str(e)}"
            }
        }
```

### 2. Elementos Chave

- **`@app.tool()`**: Este decorador é **obrigatório**. Ele registra a função com o FastMCP e a expõe para o Gemini como uma ferramenta utilizável.

- **Type Hints (Ex: `parametro1: str`)**: **Obrigatório**. O Gemini usa as anotações de tipo para entender que tipo de dado cada parâmetro espera. Sem isso, a ferramenta não funcionará corretamente.

- **Docstring**: **Obrigatório**. A docstring é a parte mais importante. O Gemini lê a descrição da função e a descrição dos `Args` para:
    1.  **Entender o propósito da ferramenta**: "Quando devo usar esta função?"
    2.  **Extrair os parâmetros**: "O que o usuário quis dizer com 'analise o repositório x'?"

- **Logging**: Adicione logs no início, no fim (sucesso) e em caso de erro. Isso é vital para a depuração.

- **Retorno com Erro**: Sempre envolva a lógica em um bloco `try...except` e retorne um dicionário estruturado de erro, conforme o padrão do projeto.

### 3. Exemplo Prático: Uma Ferramenta `get_commit_count`

Vamos supor que queremos criar uma ferramenta que conta o número de commits de um branch.

```python
@app.tool()
async def get_commit_count(repo: str, branch: str = "main") -> dict:
    """
    Conta o número de commits em um branch específico de um repositório.

    Args:
        repo: O repositório no formato 'owner/repo'.
        branch: O nome do branch. O padrão é 'main'.
    """
    logging.info(f"Contando commits para {repo} no branch {branch}")
    
    try:
        # Usamos a função centralizada de request
        response = await github_api_request(f"/repos/{repo}/commits?sha={branch}&per_page=1")
        
        if "error" in response:
            return response

        # A API do GitHub retorna o número total nos headers de paginação
        # Esta é uma forma simplificada de obter o total.
        # Em uma implementação real, seria necessário tratar a paginação.
        # Para este exemplo, vamos retornar um número fixo.
        
        commit_count = 150 # Exemplo
        
        return {"repository": repo, "branch": branch, "commit_count": commit_count}

    except Exception as e:
        logging.error(f"Erro ao contar commits para {repo}: {str(e)}")
        return {"error": {"type": "TOOL_EXECUTION_ERROR", "message": str(e)}}
```

### 4. Testando sua Nova Ferramenta

Após adicionar sua ferramenta ao `src/xcloud_mcp/main.py`, você pode testá-la diretamente através do cliente MCP (seja o Gemini, VS Code, etc.), enviando um comando em linguagem natural que você espera que ative a sua nova ferramenta.

Observe os logs do servidor para ver se a ferramenta foi chamada e qual foi o resultado.

## Fluxo de Pull Request

1.  **Fork o repositório**: Crie uma cópia do repositório na sua conta.
2.  **Crie um Branch**: Crie um branch descritivo para sua nova feature ou correção.
    ```sh
    git checkout -b feature/add-commit-counter-tool
    ```
3.  **Implemente e Teste**: Adicione sua ferramenta e teste-a localmente.
4.  **Faça o Commit**: Escreva uma mensagem de commit clara.
5.  **Abra um Pull Request**: Envie o PR para o branch `main` do repositório original.

A equipe revisará seu PR e fornecerá feedback. Obrigado por ajudar a tornar o xCloud MCP Server ainda melhor!