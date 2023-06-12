import asyncio

from blockchainapis import BlockchainAPIs
from blockchainapis.exceptions import BlockchainNotSupportedException

async def handle_throw(blockchain_id: str, api_key: str | None = None):
    async with BlockchainAPIs(api_key) as blockchain_apis:
        try:
            invalid = await blockchain_apis.exchanges(blockchain=blockchain_id)
        except BlockchainNotSupportedException:
            print(f"Blockchain with id: {blockchain_id} is not supported")

asyncio.run(handle_throw("invalid_blockchain_id"))
asyncio.run(handle_throw("ethereum", "invalid_api_key"))
