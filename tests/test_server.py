import pytest
import aiohttp
import asyncio

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio

async def test_health_check():
    """
    Tests if the /health endpoint is reachable and returns a 200 OK status.
    """
    await asyncio.sleep(30)
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get("http://mcp-server:8000/health") as response:
                assert response.status == 200
                data = await response.json()
                assert data == {"status": "ok"}
        except aiohttp.ClientConnectorError as e:
            pytest.fail(f"Could not connect to the server. Is it running? Error: {e}")