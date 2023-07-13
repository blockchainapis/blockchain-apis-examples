from typing import List

from blockchainapis import BlockchainAPIsSync
from blockchainapis.models import Reserve

def pretty_print_reserves(reserves: List[Reserve]):
    """Pretty print the reserves inside of an array

    :param reserves: The reserves returned by the API that we have to print
    :type reserves: List[Reserve]
    """
    widths = [13, 25, 42, 42, 23, 23]
    print(f'| {"Blockchain ID":<{widths[0]}} | {"Exchange ID":<{widths[1]}} | {"Token0 Address":<{widths[2]}} | {"Token1 Address":<{widths[3]}} | {"Reserve0":<{widths[4]}} | {"Reserve1":<{widths[5]}} |')
    print(f'| {"-" * widths[0]} | {"-" * widths[1]} | {"-" * widths[2]} | {"-" * widths[3]} | {"-" * widths[4]} | {"-" * widths[5]} |')
    for reserve in reserves:
        print(f'| {reserve.blockchain:<{widths[0]}} | {reserve.exchange:<{widths[1]}} | {reserve.token0:<{widths[2]}} | {reserve.token1:<{widths[3]}} | {reserve.reserve0:<{widths[4]}} | {reserve.reserve1:<{widths[5]}} |')

blockchain_apis = BlockchainAPIsSync()
# You can also get an API key at:
# https://dashboard.blockchainapis.io
# An create the instance this way:
# blockchain_apis = BlockchainAPIsSync(api_key)

# Get reserves for WETH-USDC pair on blockchain ethereum
reserves = blockchain_apis.reserves(blockchain="ethereum", token0="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", token1="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
# This method will give us the reserves inside of all of the exchanges
# available for the given pair on the given blockchain.
# If you wish to get the reserves inside of only uniswapv2_ethereum for example,
# you can call the `reserves` method this way:
# reserves = blockchain_apis.reserves(blockchain=blockchain, token0=token0, token1=token1, exchange="uniswapv2_ethereum")

# Print the reserves in an array:
pretty_print_reserves(reserves)
