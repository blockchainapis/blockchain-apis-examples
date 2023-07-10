import asyncio

from blockchainapis import BlockchainAPIs
from blockchainapis.models import Exchanges

def pretty_print_exchanges(exchanges: Exchanges):
    """Allow to pretty print exchanges in a nice array

    :param exchanges: The exchanges that we got from the API and that we are trying to print
    :type exchanges: Exchanges
    """
    widths = [25, 15, 15, 45]
    print(f'| {"Exchange ID":<{widths[0]}} | {"Blockchain ID":<{widths[1]}} | {"Exchange Name":<{widths[2]}} | {"Exchange URL":<{widths[3]}} |')
    print(f'| {"-" * widths[0]} | {"-" * widths[1]} | {"-" * widths[2]} | {"-" * widths[3]} |')
    for exchange in exchanges.data:
        print(f'| {exchange.exchange:<{widths[0]}} | {exchange.blockchain:<{widths[1]}} | {exchange.name:<{widths[2]}} | {exchange.url:<{widths[3]}} |')


# We need to create an async function, because we can't do async calls in main Python thread.
async def get_exchanges():
    # Create the Blockchain APIs instance that allow us to interact with
    # Blockchain APIs.
    # Optionaly, you can get an API key at: https://dashboard.blockchainapis.io/
    # and create a more performant instance like this:
    # async with BlockchainAPIs(API_KEY) as blockchain_apis:
    async with BlockchainAPIs() as blockchain_apis:
        exchanges = await blockchain_apis.exchanges()
        # TIP: You can select a specific blockchain by doing the following:
        # exchanges = await blockchain_apis.exchanges(blockchain="ethereum")
        pretty_print_exchanges(exchanges)

asyncio.run(get_exchanges())
