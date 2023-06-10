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

async def get_price():
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
        print("=======================")
        # We loop to get all of the results
        for amount_out in amount_outs:
            # The blockchain
            print(f"Blockchain: {amount_out.blockchain}")
            # The id of the exchange
            print(f"Exchange: {amount_out.exchange}")
            # The address of the token that we sell
            print(f"tokenIn: {amount_out.tokenIn}")
            # The address of the token that we buy
            print(f"tokenOut: {amount_out.tokenOut}")
            # The amount of tokenIn that we sell
            print(f"amountIn: {amount_out.amountIn}")
            # The amount of tokenOut that we get after selling amountIn tokenIn
            print(f"amountOut: {amount_out.amountOut}")
            print("=======================")


asyncio.run(get_price())
