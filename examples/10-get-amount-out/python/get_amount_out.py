import asyncio

from blockchainapis import BlockchainAPIs

# The blockchain that you want to get the price from
BLOCKCHAIN = "ethereum"

# The address of the token that we are selling
# Here we put the address of wrapped ETH
TOKEN_IN = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

# The address of the token that we are buying
# Here we put USDC
TOKEN_OUT = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

# The amount of TOKEN_IN that we are selling.
# We add 10**18 because the TOKEN_IN is WETH and WETH has
# 18 decimals
AMOUNT_IN = 1 * 10**18

async def get_amount_out():
    # Create the blockchain APIs instance that will automatically
    # free its resources.
    # You can also get an API key for free at: https://dashboard.blockchainapis.io
    # and create the instance the instance like this:
    # async with BlockchainAPIs(api_key) as blockchain_apis:
    async with BlockchainAPIs() as blockchain_apis:
        amount_outs = await blockchain_apis.amount_out(
            blockchain=BLOCKCHAIN,
            tokenIn=TOKEN_IN,
            tokenOut=TOKEN_OUT,
            amountIn=AMOUNT_IN
        )

        # We get the decimals of the token out to format the output:
        token_out_decimals = await blockchain_apis.decimals(BLOCKCHAIN, TOKEN_OUT)

        # We loop to get all of the results
        for amount_out in amount_outs:
            print(f"{amount_out.exchange} will give you {blockchain_apis.get_token_decimal_form(amount_out.amountOut, token_out_decimals)} USDC")


asyncio.run(get_amount_out())
