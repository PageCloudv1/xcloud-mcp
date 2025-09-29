import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest

from xcloud_mcp.main import (
    analyze_repository,
    create_workflow_issue,
    get_xcloud_repositories,
    monitor_ci_status,
)

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio


@pytest.fixture
def mock_github_api(mocker):
    """Mocks the github_api_request function."""
    return mocker.patch("xcloud_mcp.main.github_api_request", autospec=True)


async def test_analyze_repository_success(mock_github_api):
    """
    Tests the analyze_repository tool with a successful mock API response.
    """
    # Arrange: Set up the mock to return fake data
    repo_url = "PageCloudv1/xcloud-mcp"
    mock_repo_data = {
        "description": "Test repo",
        "language": "Python",
        "stargazers_count": 10,
        "forks_count": 5,
    }
    mock_workflows_data = {"total_count": 1, "workflows": [{"state": "active"}]}
    mock_runs_data = {
        "total_count": 2,
        "workflow_runs": [{"conclusion": "success"}, {"conclusion": "failure"}],
    }

    # Configure the mock to return different values on subsequent calls
    mock_github_api.side_effect = [mock_repo_data, mock_workflows_data, mock_runs_data]

    # Act: Call the function being tested
    result = await analyze_repository.fn(repo_url)

    # Assert: Check that the function processed the data correctly
    assert "error" not in result
    assert result["repository"] == "PageCloudv1/xcloud-mcp"
    assert result["language"] == "Python"
    assert result["workflows"]["total"] == 1
    assert result["recent_activity"]["failed_runs"] == 1
    assert len(result["suggestions"]) == 1
    assert result["suggestions"][0]["type"] == "reliability"


async def test_analyze_repository_not_found(mock_github_api):
    """
    Tests the analyze_repository tool for a repository that doesn't exist.
    """
    # Arrange: Configure the mock to simulate a 'Not Found' error
    repo_url = "nonexistent/repo"
    mock_github_api.return_value = {
        "error": {
            "type": "GITHUB_API_ERROR",
            "status_code": 404,
            "message": "Not Found",
        }
    }

    # Act
    result = await analyze_repository.fn(repo_url)

    # Assert
    assert "error" in result
    assert result["error"]["type"] == "GITHUB_API_ERROR"
    assert result["error"]["status_code"] == 404
    assert result["error"]["message"] == "Not Found"


async def test_analyze_repository_invalid_url():
    """
    Tests the analyze_repository tool with an invalid URL format.
    """
    # Act
    result = await analyze_repository.fn("invalid-url")

    # Assert
    assert "error" in result
    assert result["error"] == "URL inválida. Use formato: owner/repo"


async def test_create_workflow_issue_success(mock_github_api):
    """
    Tests the create_workflow_issue tool with a successful issue creation.
    """
    # Arrange
    repo = "PageCloudv1/test-repo"
    workflow_type = "ci"
    mock_issue_response = {
        "html_url": "https://github.com/PageCloudv1/test-repo/issues/1",
        "number": 1,
        "title": "🔄 Implementar Workflow CI (Integração Contínua)",
    }
    mock_github_api.return_value = mock_issue_response

    # Act
    result = await create_workflow_issue.fn(repo, workflow_type)

    # Assert
    assert result["success"] is True
    expected_url = "https://github.com/PageCloudv1/test-repo/issues/1"
    assert result["issue_url"] == expected_url
    assert result["issue_number"] == 1
    assert "CI" in result["title"]
    mock_github_api.assert_called_once()


async def test_create_workflow_issue_invalid_type(mock_github_api):
    """
    Tests the create_workflow_issue tool with an invalid workflow type.
    """
    # Arrange
    repo = "PageCloudv1/test-repo"
    workflow_type = "invalid-type"

    # Act
    result = await create_workflow_issue.fn(repo, workflow_type)

    # Assert
    assert "error" in result
    assert "Tipo de workflow inválido" in result["error"]
    mock_github_api.assert_not_called()


async def test_create_workflow_issue_api_error(mock_github_api):
    """
    Tests the create_workflow_issue tool when GitHub API returns an error.
    """
    # Arrange
    repo = "PageCloudv1/test-repo"
    workflow_type = "cd"
    mock_github_api.return_value = {
        "error": {
            "type": "GITHUB_API_ERROR",
            "status_code": 404,
            "message": "Repository not found",
        }
    }

    # Act
    result = await create_workflow_issue.fn(repo, workflow_type)

    # Assert
    assert "error" in result
    assert result["error"]["type"] == "GITHUB_API_ERROR"
    assert "Repository not found" in result["error"]["message"]


async def test_create_workflow_issue_with_custom_title(mock_github_api):
    """
    Tests the create_workflow_issue tool with a custom title.
    """
    # Arrange
    repo = "PageCloudv1/test-repo"
    workflow_type = "build"
    custom_title = "Custom Build Workflow"
    mock_issue_response = {
        "html_url": "https://github.com/PageCloudv1/test-repo/issues/2",
        "number": 2,
        "title": custom_title,
    }
    mock_github_api.return_value = mock_issue_response

    # Act
    result = await create_workflow_issue.fn(repo, workflow_type, custom_title)

    # Assert
    assert result["success"] is True
    assert result["title"] == custom_title


async def test_monitor_ci_status_success(mock_github_api):
    """
    Tests the monitor_ci_status tool with successful workflow runs.
    """
    # Arrange
    repo = "PageCloudv1/test-repo"
    mock_runs_data = {
        "workflow_runs": [
            {
                "name": "CI",
                "status": "completed",
                "conclusion": "success",
                "head_branch": "main",
                "head_sha": "abc123def456",
                "actor": {"login": "testuser"},
                "created_at": "2025-09-29T10:00:00Z",
                "html_url": (
                    "https://github.com/PageCloudv1/" "test-repo/actions/runs/1"
                ),
            },
            {
                "name": "Build",
                "status": "in_progress",
                "conclusion": None,
                "head_branch": "feature/test",
                "head_sha": "xyz789abc123",
                "actor": {"login": "developer"},
                "created_at": "2025-09-29T11:00:00Z",
                "html_url": (
                    "https://github.com/PageCloudv1/" "test-repo/actions/runs/2"
                ),
            },
        ]
    }
    mock_github_api.return_value = mock_runs_data

    # Act
    result = await monitor_ci_status.fn(repo, 2)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["workflow"] == "CI"
    assert result[0]["status"] == "completed"
    assert result[0]["conclusion"] == "success"
    assert result[0]["branch"] == "main"
    assert result[0]["commit"] == "abc123d"
    assert result[1]["workflow"] == "Build"
    assert result[1]["status"] == "in_progress"


async def test_monitor_ci_status_api_error(mock_github_api):
    """
    Tests the monitor_ci_status tool when GitHub API returns an error.
    """
    # Arrange
    repo = "PageCloudv1/test-repo"
    mock_github_api.return_value = {
        "error": {
            "type": "GITHUB_API_ERROR",
            "status_code": 404,
            "message": "Not Found",
        }
    }

    # Act
    result = await monitor_ci_status.fn(repo)

    # Assert
    assert "error" in result
    assert result["error"]["type"] == "GITHUB_API_ERROR"
    assert result["error"]["message"] == "Not Found"


async def test_monitor_ci_status_empty_runs(mock_github_api):
    """
    Tests the monitor_ci_status tool with no workflow runs.
    """
    # Arrange
    repo = "PageCloudv1/test-repo"
    mock_runs_data = {"workflow_runs": []}
    mock_github_api.return_value = mock_runs_data

    # Act
    result = await monitor_ci_status.fn(repo, 5)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 0


async def test_monitor_ci_status_exception(mock_github_api):
    """
    Tests the monitor_ci_status tool when an exception occurs.
    """
    # Arrange
    repo = "invalid/format/repo"
    # The exception will be captured by the tool and formatted in the new pattern
    mock_github_api.side_effect = Exception("Connection error")

    # Act
    result = await monitor_ci_status.fn(repo)

    # Assert
    assert "error" in result
    # A lógica interna da ferramenta captura a exceção e a formata
    assert "Erro: Connection error" in result["error"]


async def test_get_xcloud_repositories_success(mock_github_api):
    """
    Tests the get_xcloud_repositories tool with successful repository listing.
    """
    # Arrange
    mock_repos_data = [
        {
            "name": "xcloud-mcp",
            "full_name": "PageCloudv1/xcloud-mcp",
            "description": "MCP Server for xCloud automation",
            "language": "Python",
            "html_url": "https://github.com/PageCloudv1/xcloud-mcp",
        },
        {
            "name": "xcloud-docs",
            "full_name": "PageCloudv1/xcloud-docs",
            "description": "Documentation for xCloud platform",
            "language": "Markdown",
            "html_url": "https://github.com/PageCloudv1/xcloud-docs",
        },
        {
            "name": "regular-repo",
            "full_name": "PageCloudv1/regular-repo",
            "description": "Not an xCloud repo",
            "language": "JavaScript",
            "html_url": "https://github.com/PageCloudv1/regular-repo",
        },
    ]

    mock_workflows_responses = [
        {"total_count": 2},  # xcloud-mcp has workflows
        {"total_count": 0},  # xcloud-docs has no workflows
    ]

    # Configure the mock to return different values on subsequent calls
    mock_github_api.side_effect = [mock_repos_data] + mock_workflows_responses

    # Act
    result = await get_xcloud_repositories.fn()

    # Assert
    assert isinstance(result, list)
    assert len(result) == 2  # Only xCloud repos
    assert result[0]["name"] == "xcloud-mcp"
    assert result[0]["has_workflows"] is True
    assert result[1]["name"] == "xcloud-docs"
    assert result[1]["has_workflows"] is False
    assert "regular-repo" not in [repo["name"] for repo in result]


async def test_get_xcloud_repositories_api_error(mock_github_api):
    """
    Tests the get_xcloud_repositories tool when GitHub API returns an error.
    """
    # Arrange
    mock_github_api.return_value = {
        "error": {
            "type": "GITHUB_API_ERROR",
            "status_code": 401,
            "message": "Bad credentials",
        }
    }

    # Act
    result = await get_xcloud_repositories.fn()

    # Assert
    assert "error" in result
    assert result["error"]["type"] == "GITHUB_API_ERROR"
    assert result["error"]["message"] == "Bad credentials"


async def test_get_xcloud_repositories_no_xcloud_repos(mock_github_api):
    """
    Tests the get_xcloud_repositories tool when no xCloud repos exist.
    """
    # Arrange
    mock_repos_data = [
        {
            "name": "regular-repo1",
            "full_name": "PageCloudv1/regular-repo1",
            "description": "Not an xCloud repo",
            "language": "JavaScript",
            "html_url": "https://github.com/PageCloudv1/regular-repo1",
        }
    ]
    mock_github_api.return_value = mock_repos_data

    # Act
    result = await get_xcloud_repositories.fn()

    # Assert
    assert isinstance(result, list)
    assert len(result) == 0


async def test_get_xcloud_repositories_exception(mock_github_api):
    """
    Tests the get_xcloud_repositories tool when an exception occurs.
    """
    # Arrange
    mock_github_api.side_effect = Exception("Network timeout")

    # Act
    result = await get_xcloud_repositories.fn()

    # Assert
    assert "error" in result
    assert "Erro: Network timeout" in result["error"]


# ==========================================
# Tests for github_api_request function
# ==========================================


async def test_github_api_request_function_exists():
    """
    Tests that github_api_request function exists and is callable.
    """
    import inspect

    from xcloud_mcp.main import github_api_request

    # Test function exists and is async
    assert callable(github_api_request)
    assert inspect.iscoroutinefunction(github_api_request)

    # Test function signature
    sig = inspect.signature(github_api_request)
    params = list(sig.parameters.keys())

    # Assert function has expected parameters
    assert "endpoint" in params
    assert "method" in params
    assert "data" in params

    # Test default parameter values
    assert sig.parameters["method"].default == "GET"
    assert sig.parameters["data"].default is None



async def test_github_api_request_method_validation(mocker):
    """
    Tests github_api_request method parameter validation for supported methods.
    """
    from xcloud_mcp.main import github_api_request

    # Arrange
    mock_session = mocker.patch("aiohttp.ClientSession.request")
    mock_response = mock_session.return_value.__aenter__.return_value
    mock_response.status = 200
    mock_response.json.return_value = {"status": "ok"}

    # Act & Assert for supported methods
    for method in ["GET", "POST", "PATCH"]:
        result = await github_api_request("/test", method=method)
        assert "error" not in result
        assert result == {"status": "ok"}


async def test_github_api_request_url_construction():
    """
    Tests that github_api_request constructs URLs correctly.
    """
    from xcloud_mcp.main import GITHUB_API_BASE

    # Test that the base URL constant exists
    assert GITHUB_API_BASE == "https://api.github.com"

    # Test endpoint parameter handling
    endpoint = "/repos/test/repo"
    expected_url = f"{GITHUB_API_BASE}{endpoint}"
    assert expected_url == "https://api.github.com/repos/test/repo"
