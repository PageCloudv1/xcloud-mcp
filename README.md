# 🤖 xCloud Bot - MCP Server

FastMCP server for integration with AI and automation tools.

## 🚀 Getting Started

This project is containerized using Podman and configured for development with VS Code.

### Prerequisites

- [Podman](https://podman.io/getting-started/installation)
- [podman-compose](https://github.com/containers/podman-compose)
- [VS Code](https://code.visualstudio.com/)
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd xcloud-mcp
    ```

2.  **Create the environment file:**

    Create a `.env` file in the root of the project and add your API keys.

    ```env
    # .env
    GITHUB_TOKEN=your_github_personal_access_token
    GEMINI_API_KEY=your_gemini_api_key
    ```

3.  **Open with VS Code:**
    ```bash
    code .
    ```

## 💻 Development Workflow

### Running the Application

1.  Open the Command Palette (`Ctrl+Shift+P`).
2.  Run the task **`Tasks: Run Build Task`**. This will execute the default `Compose Up (Dev)` task.
3.  This builds the development container and starts the server with hot-reloading enabled.

### Debugging the Application

1.  Ensure the application is running via the `Compose Up (Dev)` task.
2.  Go to the "Run and Debug" panel in VS Code.
3.  Select **`Python: Attach to App`** from the dropdown and click the green play button.
4.  The debugger will attach to the running server. You can now set breakpoints in `server.py`.

## 🧪 Testing Workflow

### Running Tests

1.  Open the Command Palette (`Ctrl+Shift+P`).
2.  Run the task **`Tasks: Run Task`** and select **`Run Tests`**.
3.  This will build the test container and run the `pytest` suite. The output will be shown in the terminal.

### Debugging Tests

1.  Open the Command Palette (`Ctrl+Shift+P`) and run the task **`Debug Tests`**. This will start the test container and wait for a debugger to attach.
2.  Go to the "Run and Debug" panel.
3.  Select **`Python: Attach to Tests`** from the dropdown and click the green play button.
4.  The debugger will attach to the test runner. You can now set breakpoints in your test files (e.g., `tests/test_server.py`).

## 🛑 Stopping the Application

- To stop the main application or the debug test server, open the Command Palette (`Ctrl+Shift+P`) and run the task **`Compose Down`**.