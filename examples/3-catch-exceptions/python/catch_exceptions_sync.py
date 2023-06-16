from blockchainapis import BlockchainAPIsSync

# Import all exceptions
from blockchainapis.exceptions import BlockchainNotSupportedException
from blockchainapis.exceptions import UnauthorizedException
from blockchainapis.exceptions import BlockchainAPIsException
from blockchainapis.exceptions import UnknownBlockchainAPIsException

def handle_throw(blockchain_id: str, api_key: str | None = None):
    blockchain_apis = BlockchainAPIsSync(api_key)
    try:
        invalid = blockchain_apis.exchanges(blockchain=blockchain_id)
    except BlockchainNotSupportedException:
        # Catch in case the given blockchain id is invalid
        print(f"Blockchain with id: {blockchain_id} is not supported")
    except UnauthorizedException:
        # Catch in case the given API key is invalid
        print(f"Given API key: {api_key} is not a valid API key")
        print("To fix this error, get an API key at: https://dashboard.blockchainapis.io/")
    except UnknownBlockchainAPIsException as e:
        # Catch in case an unknown Exception is thrown, this should not happen.
        print(f"An unknown exception has hapenned:")
        print(e)
    except BlockchainAPIsException as e:
        # Catch in case any exception is thrown from Blockchain APIs.
        # try to comment all of the except above and see what happens
        print(f"Got an exception from the API:", e)

handle_throw("invalid_blockchain_id")
handle_throw("ethereum", "invalid_api_key")
