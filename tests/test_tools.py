import pytest
from src.xcloud_mcp.main import analyze_repository

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio

@pytest.fixture
def mock_github_api(mocker):
    """Mocks the github_api_request function."""
    return mocker.patch('src.xcloud_mcp.main.github_api_request', autospec=True)

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
        "forks_count": 5
    }
    mock_workflows_data = {"total_count": 1, "workflows": [{"state": "active"}]}
    mock_runs_data = {"total_count": 2, "workflow_runs": [
        {"conclusion": "success"},
        {"conclusion": "failure"}
    ]}

    # Configure the mock to return different values on subsequent calls
    mock_github_api.side_effect = [
        mock_repo_data,
        mock_workflows_data,
        mock_runs_data
    ]

    # Act: Call the function being tested
    result = await analyze_repository(repo_url)

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
    mock_github_api.return_value = {"message": "Not Found"}

    # Act
    result = await analyze_repository(repo_url)

    # Assert
    assert "error" in result
    assert result["error"] == "Repositório não encontrado: Not Found"

async def test_analyze_repository_invalid_url():
    """
    Tests the analyze_repository tool with an invalid URL format.
    """
    # Act
    result = await analyze_repository("invalid-url")

    # Assert
    assert "error" in result
    assert result["error"] == "URL inválida. Use formato: owner/repo"
