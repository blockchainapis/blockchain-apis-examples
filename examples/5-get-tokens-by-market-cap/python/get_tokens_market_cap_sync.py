from typing import List

from blockchainapis import BlockchainAPIsSync
from blockchainapis.models import Token

def pretty_print_tokens(tokens: List[Token]):
    """Print the given tokens inside of an array

    :param token: The list of tokens to print
    :type token: Token
    """
    widths = [42, 15, 8, 24]
    print(f'| {"Token Address":<{widths[0]}} | {"Blockchain ID":<{widths[1]}} | {"Decimals":<{widths[2]}} | {"Market Cap":<{widths[3]}} |')
    print(f'| {"-" * widths[0]} | {"-" * widths[1]} | {"-" * widths[2]} | {"-" * widths[3]} |')
    for token in tokens:
        print(f'| {token.address:<{widths[0]}} | {token.blockchain:<{widths[1]}} | {token.decimals:<{widths[2]}} | {token.market_cap:<{widths[3]}} |')

# Create the blockchain APIs instance to interact with Blockchain APIs
# You can also optionally get an API key at:
# https://dashboard.blockchainapis.io
# An create the instance this way:
# blockchain_apis = BlockchainAPIsSync(api_key)
blockchain_apis = BlockchainAPIsSync()

# Make the call to blockchain_apis in order to get the tokens
# of the ethereum blockchain
tokens = blockchain_apis.tokens(blockchain="ethereum")
# Please note that you can call the `tokens` method without any arguments:
# tokens = blockchain_apis.tokens()
# This way, it will give you the market cap of all of the tokens regardless of
# the blockchain

# Print the current page that we are at.
print(f"Current page: {tokens.page}")
# Blockchain APIs only returns 100 result per page.
# If you are willing to see the next page, you can call
# the api this way:
# tokens = blockchain_apis.tokens(page=2, blockchain=blockchain)

# Print the total amount of pages:
print(f"Total pages: {tokens.total_pages}")

# tokens.data contains the list of tokens, we use the pretty_print_token
# method in order to pretty print the top 10 tokens
pretty_print_tokens(tokens.data[:10])
