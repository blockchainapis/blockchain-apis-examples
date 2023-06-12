import asyncio

from blockchainapis import BlockchainAPIs

# We create an Async function because we can't use async in the main Python thread
async def get_blockchains():
    # Create the Blockchain APIs instance that allow us to interact with
    # Blockchain APIs.
    # Optionaly, you can get an API key at: https://dashboard.blockchainapis.io/
    # and create a more performant instance like this:
    # async with BlockchainAPIs(API_KEY) as blockchain_apis:
    async with BlockchainAPIs() as blockchain_apis:
        # Make an API call in order to get the list of blockchains.
        blockchains = await blockchain_apis.blockchains()
        # print("=======================")
        # The returned result is a list, so we need to loop throught the result
        for blockchain in blockchains:
            print(f"- {blockchain.blockchain}")
            # Print the name of the blockchain
            # print(f"Blockchain name: {blockchain.name}")
            # Print the id of the blockchain:
            # print(f"Blockchain id: {blockchain.blockchain}")
            # Print the chain id
            # print(f"Chain id: {blockchain.chain_id}")
            # Print the url to the explorer of the blockchain:
            # print(f"Blockchain explorer: {blockchain.explorer}")
            # print("=======================")

# Run the async function
asyncio.run(get_blockchains())
