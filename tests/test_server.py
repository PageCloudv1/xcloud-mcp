import pytest
import aiohttp
import asyncio

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio

async def test_health_check():
    """
    Tests if the /health endpoint is reachable and returns a 200 OK status.
    """
    # Give the server a moment to start up inside the container
    await asyncio.sleep(2)
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get("http://localhost:8000/health") as response:
                assert response.status == 200
                data = await response.json()
                assert data == {"status": "ok"}
        except aiohttp.ClientConnectorError as e:
            pytest.fail(f"Could not connect to the server. Is it running? Error: {e}")