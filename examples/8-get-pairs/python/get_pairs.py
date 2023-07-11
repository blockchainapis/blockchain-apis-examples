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
        # pairs = await blockchain_apis.pairs(blockchain="ethereum")
        print(pairs)
        # There are 100 results per page
        # by default we start at page 1
        print(f"Current page: {pairs.page}")
        # We print the total amount of pages:
        print(f"Total pages: {pairs.total_pages}")
        # TIP: You can choose which page you want to get by doing the following:
        # pairs = await blockchain_apis.pairs(page=2)
        
        # Now we get the first pair available:
        pair = pairs.data[0]
        print("First pair:")
        # The id of the blockchain on which the pair is
        print(f"Blockchain ID of pair: {pair.blockchain}")
        # The id of the exchange on which the pair is
        print(f"Exchange ID of pair: {pair.exchange}")
        # A pair contains two tokens: token0 and token1
        # In order to be able to execute a trade in any of these pairs, you will need
        # to own some token0 or token1.
        print(f"Token0 of pair: {pair.token0}")
        print(f"Token1 of pair: {pair.token1}")
        # The fee taken by liquidity providers during a trade
        print(f"fee: {pair.fee}")

asyncio.run(get_pairs())
