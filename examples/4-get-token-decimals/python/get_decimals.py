import asyncio

from blockchainapis import BlockchainAPIs

# The id of the blockchain that you want to get the decimals from.
#
# If you want to get the list of valid blockchain ids, you can follow this tutorial:
# https://docs.blockchainapis.io/docs/tutorial/getting-started/get-supported-blockchains
BLOCKCHAIN = "ethereum"

# The token that you want to get the decimals from
# Here: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2, is the address of the WETH
# token.
TARGET_TOKEN = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

async def get_decimals(blockchain: str, token: str):
    # Create the Blockchain APIs instance that allow us to interact with
    # Blockchain APIs.
    # Optionaly, you can get an API key at: https://dashboard.blockchainapis.io/
    # and create a more performant instance like this:
    # async with BlockchainAPIs(API_KEY) as blockchain_apis:
    async with BlockchainAPIs() as blockchain_apis:
        # Make the call to blockchain_apis
        token_decimals = await blockchain_apis.decimals(blockchain=blockchain, token=token)

        print(f"Token at address {token} have {token_decimals} decimals.")

asyncio.run(get_decimals(BLOCKCHAIN, TARGET_TOKEN))
