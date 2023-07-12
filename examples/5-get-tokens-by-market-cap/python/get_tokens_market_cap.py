import asyncio

from typing import List

from blockchainapis import BlockchainAPIs
from blockchainapis.models import Token

def find_token_in_data(token_to_find: str, data: List[Token]) -> Token:
    """Allow us to find a specific token inside of the given data list

    :param data: The data returned by the API
    :type data: List[Token]
    :return: The token that we are looking for
    :rtype: Token
    """
    for token in data:
        if token.address == token_to_find:
            return token
        
    raise Exception(f"Token {token_to_find} could not be found inside of the data")

def pretty_print_tokens(tokens: List[Token]):
    """Print the given tokens in a pretty print way

    :param token: The list of tokens to print
    :type token: Token
    """

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

        # tokens.data contains the list of all of the tokens ordered by Market cap.
        # We use the function below in order to find the market cap of WETH
        weth_token = find_token_in_data("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", tokens.data)
        # Same for WBTC.
        wbtc_token = find_token_in_data("0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", tokens.data)
        # Please note: The address of WETH and WBTC can easily be found on google by searching:
        # "WETH address" and "WBTC address"

        # We use the pretty_print_token method in order to pretty print the given tokens
        pretty_print_tokens([weth_token, wbtc_token])

asyncio.run(get_tokens_by_market_cap("ethereum"))
