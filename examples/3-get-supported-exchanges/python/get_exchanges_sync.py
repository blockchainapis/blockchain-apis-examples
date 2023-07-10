from blockchainapis import BlockchainAPIsSync
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


blockchain_apis = BlockchainAPIsSync()
# You can also get an API key at:
# https://dashboard.blockchainapis.io
# An create the instance this way:
# blockchain_apis = BlockchainAPIsSync(api_key)

# Get the available exchanges for all of the blockchains
exchanges = blockchain_apis.exchanges()
# TIP, you can also do the following to only get the exchanges from
# a specific blockchain:
# exchanges = blockchain_apis.exchanges(blockchain="ethereum")

# pretty print the exchanges inside of an array
pretty_print_exchanges(exchanges)
