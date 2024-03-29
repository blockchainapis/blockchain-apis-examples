from blockchainapis import BlockchainAPIsSync

# Create the blockchain APIs instance to interact with Blockchain APIs
# You can also optionally get an API key at:
# https://dashboard.blockchainapis.io
# An create the instance this way:
# blockchain_apis = BlockchainAPIsSync(api_key)
blockchain_apis = BlockchainAPIsSync()

def get_decimal_form(blockchain: str, token: str, amount: int, name: str):
    """Get the decimal form of the token for the given amount and
    prints it.

    :param blockchain: The id of the blockchain that the token is
    :type blockchain: str
    :param token: The address of the token
    :type token: str
    :param amount: The amount that we have to convert
    :type amount: int
    :param name: The name of the token
    :type name: str
    """
    # Get the amount of decimals that the token has
    decimals = blockchain_apis.decimals(blockchain, token)
    # Get the decimal form of the token from the amount of decimals
    decimal_form = blockchain_apis.get_token_decimal_form(amount=amount, decimals=decimals)
    print(f"{amount} {token} in decimal is: {decimal_form} {name}")

def to_unsigned_form(blockchain: str, token: str, decimal_amount: str, name: str):
    """Transform a token amount in decimal form to his unsigned integer form

    :param blockchain: The id of the blockchain on which you want to make the trade
    :type blockchain: str
    :param token: The address of the token that we are buying
    :type token: str
    :param decimal_amount: The amount in decimal form of the given token
    :type decimal_amount: str
    :param name: The name of the given token
    :type name: str
    """
    # Get the amount of decimals that the token has
    decimals = blockchain_apis.decimals(blockchain, token)
    # Get the unsigned integer form of the token from the amount of decimals
    unsigned_form = blockchain_apis.get_token_unsigned_form(amount=decimal_amount, decimals=decimals)
    print(f"{decimal_amount} {name} in unsigned integer form is: {unsigned_form} {token}")

get_decimal_form("ethereum", "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", 2450000000000000000, "WETH")
to_unsigned_form("ethereum", "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "2542.42", "USDC")
