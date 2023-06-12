import asyncio

from blockchainapis import BlockchainAPIs

# Import all exceptions
from blockchainapis.exceptions import BlockchainNotSupportedException
from blockchainapis.exceptions import UnauthorizedException
from blockchainapis.exceptions import BlockchainAPIsException

async def handle_throw(blockchain_id: str, api_key: str | None = None):
    async with BlockchainAPIs(api_key) as blockchain_apis:
        try:
            invalid = await blockchain_apis.exchanges(blockchain=blockchain_id)
        except BlockchainNotSupportedException:
            # Catch in case the given blockchain id is invalid
            print(f"Blockchain with id: {blockchain_id} is not supported")
        except UnauthorizedException:
            # Catch in case the given API key is invalid
            print(f"Given API key: {api_key} is not valid")
        except BlockchainAPIsException as e:
            # Catch in case any exception is thrown from Blockchain APIs.
            # try to comment all of the except above and see what happens
            print(f"Got an exception from the API:", e)
        except Exception as e:
            # Catch when an exceptions is thrown that is not related to the API
            print(f"Got an exception that is not related to Blockchain APIs:", e)

asyncio.run(handle_throw("invalid_blockchain_id"))
asyncio.run(handle_throw("ethereum", "invalid_api_key"))
