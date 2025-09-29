import pytest
import aiohttp
import asyncio

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio

# async def test_health_check():
#     """
#     Tests if the /health endpoint is reachable and returns a 200 OK status.
#     """
#     max_wait_time = 60  # seconds
#     wait_interval = 2  # seconds
#     start_time = asyncio.get_event_loop().time()

#     async with aiohttp.ClientSession() as session:
#         while True:
#             try:
#                 async with session.get("http://localhost:8000/health") as response:
#                     if response.status == 200:
#                         data = await response.json()
#                         assert data == {"status": "ok"}
#                         return  # Test passed
#             except aiohttp.ClientConnectorError:
#                 pass  # Ignore connection errors and retry

#             if asyncio.get_event_loop().time() - start_time > max_wait_time:
#                 pytest.fail(
#                     "Could not connect to the server within the timeout period. "
#                     "Is it running and accessible at http://localhost:8000?"
#                 )
            
#             await asyncio.sleep(wait_interval)