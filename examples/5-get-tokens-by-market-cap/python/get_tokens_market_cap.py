import asyncio

from typing import List

from blockchainapis import BlockchainAPIs
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


async def get_tokens_by_market_cap(blockchain: str):
    # Create the Blockchain APIs instance that allow us to interact with
    # Blockchain APIs.
    # Optionaly, you can get an API key at: https://dashboard.blockchainapis.io/
    # and create a more performant instance like this:
    # async with BlockchainAPIs(API_KEY) as blockchain_apis:
    async with BlockchainAPIs() as blockchain_apis:
        # Make the call to blockchain_apis to get the tokens
        tokens = await blockchain_apis.tokens(blockchain=blockchain)
        # Here we put the blockchain with the given id: blockchain
        # But we could call it without any blockchain:
        # tokens = await blockchain_apis.tokens()
        # Which will give us all of the tokens supported by Blockchain APIs for all of
        # the blockchains.
        
        # Print the current page that we are at.
        print(f"Current page: {tokens.page}")
        # Blockchain APIs only returns 100 result per page.
        # If you are willing to see the next page, you can call
        # the api this way:
        # tokens = await blockchain_apis.tokens(page=2, blockchain=blockchain)

        # Print the total amount of pages:
        print(f"Total pages: {tokens.total_pages}")

        # tokens.data contains the list of tokens, we use the pretty_print_token
        # method in order to pretty print the top 10 tokens
        pretty_print_tokens(tokens.data[:10])

asyncio.run(get_tokens_by_market_cap("ethereum"))
