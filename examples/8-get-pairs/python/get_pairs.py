import asyncio

from blockchainapis import BlockchainAPIs


# We need to create an async function, because we can't do async calls in main Python thread.
async def get_pairs():
    # Create the Blockchain APIs instance that allow us to interact with
    # Blockchain APIs.
    # Optionaly, you can get an API key at: https://dashboard.blockchainapis.io/
    # and create a more performant instance like this:
    # async with BlockchainAPIs(API_KEY) as blockchain_apis:
    async with BlockchainAPIs() as blockchain_apis:
        # Get pairs for every blockchain
        pairs = await blockchain_apis.pairs()
        # TIP: You can specify a specific blockchain id by doing the folowing:
        # blockchain_apis.pairs(blockchain="ethereum")
        print(pairs)

asyncio.run(get_pairs())
