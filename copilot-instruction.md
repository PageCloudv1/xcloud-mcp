# GitHub Copilot Instructions for the xCloud MCP Server

This document provides context and guidelines for GitHub Copilot to assist in the development of the `xCloud MCP Server`.

## 1. Project Overview

- **Project Name:** xCloud MCP (Master Control Program) Server.
- **Purpose:** This is a Python-based backend service that exposes a set of tools (functions) for AI agents and other services. It primarily integrates with the GitHub API and Google Gemini to automate DevOps tasks like repository analysis, issue creation, and CI/CD monitoring.
- **Framework:** The server is built using `FastMCP`, a lightweight framework for creating tool-based applications.

## 2. Core Technologies

- **Language:** Python 3.11+
- **Framework:** `FastMCP`
- **Asynchronous Programming:** `asyncio` is used extensively. All I/O operations (like API calls) must be non-blocking. Use `async def` for functions and `await` for calls.
- **HTTP Client:** `aiohttp` is the standard for making asynchronous HTTP requests to external APIs (e.g., GitHub API).
- **Containerization:** The project is designed to be run inside a container using `Podman`. The configuration is defined in a `Containerfile`.

## 3. Coding Style and Conventions

- **Style Guide:** Strictly follow **PEP 8**. Use an autoformatter like `black` if possible.
- **Type Hinting:** All function signatures **must** include type hints (`from typing import ...`). This is critical for code clarity and maintainability.
- **Asynchronous Functions:** All functions that perform I/O (network requests, file system access) **must** be defined with `async def`.
- **Error Handling:** Use `try...except` blocks to gracefully handle potential errors, especially around API calls and command execution. Return a dictionary with an `"error"` key to indicate failure.
- **Configuration:** All configuration values (API keys, tokens, etc.) **must** be loaded from environment variables using `os.getenv()`. Do not hardcode secrets.
- **Logging:** Use simple `print()` statements for now, but be prepared to integrate a structured logger like `winston` or Python's `logging` module.

## 4. Architectural Patterns

- **Tool-Based Architecture:** The core of the application is defining "tools" using the `@app.tool()` decorator from `FastMCP`. Each tool should be a self-contained, asynchronous function that performs a specific action.
- **Single Responsibility:** Each tool should do one thing well. For example, `analyze_repository` analyzes a repo, and `create_workflow_issue` creates an issue.
- **Statelessness:** The server should be stateless. Do not store application state in global variables.

## 5. How to Generate Code

- **When creating a new tool:**
  - Use the `@app.tool()` decorator.
  - The function **must** be `async def`.
  - Include a clear docstring explaining what the tool does, its arguments (`Args:`), and what it returns.
  - Use `aiohttp` for any external API calls.
  - Return a JSON-serializable dictionary.

- **When writing comments:**
  - Focus on *why* something is done, not *what* is being done. The code and type hints should explain the "what".
  - Use docstrings for all public functions and modules.

- **Example of a well-defined tool:**

  ```python
  from fastmcp import FastMCP
  from typing import Dict
  import os
  import aiohttp

  app = FastMCP("xcloud-bot")
  GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

  @app.tool()
  async def get_repo_details(repo_name: str) -> Dict:
      """
      Fetches details for a specific GitHub repository.

      Args:
          repo_name: The name of the repository in "owner/repo" format.
      """
      headers = {
          "Authorization": f"token {GITHUB_TOKEN}",
          "Accept": "application/vnd.github.v3+json"
      }
      url = f"https://api.github.com/repos/{repo_name}"

      try:
          async with aiohttp.ClientSession() as session:
              async with session.get(url, headers=headers) as response:
                  response.raise_for_status() # Raise an exception for bad status codes
                  return await response.json()
      except aiohttp.ClientError as e:
          print(f"Error fetching repository details: {e}")
          return {"error": str(e)}
  ```
