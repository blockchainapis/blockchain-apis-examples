import asyncio

from blockchainapis import BlockchainAPIs

async def get_amount_in():
    # Create the blockchain APIs instance that will automatically
    # free its resources.
    # You can also get an API key for free at: https://dashboard.blockchainapis.io
    # and create the instance the instance like this:
    # async with BlockchainAPIs(api_key) as blockchain_apis:
    async with BlockchainAPIs() as blockchain_apis:
        amounts_in = await blockchain_apis.amount_in(
            # The blockchain on which you want the exchange to take place
            blockchain="ethereum",
            # The address of the token that you sell, here it is WETH address
            tokenIn="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
            # The address of the token that we buy, here it is USDC
            tokenOut="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            # The amount of tokenOut that we are willing to get.
            # Here we want to get 2000 USDC.
            # We need to add 10**6 because the USDC token has 6 decimals
            amountOut=2000 * 10**6,
            # You can optionally set a specific exchange id in order to get the rate
            # on a specific exchange, for example if you want to use Uniswap:
            # exchange="uniswapv2_ethereum"
            # By default, if you don't specify an exchange, it will give you the amount
            # out for every exchange available.
        )

        # We loop to get all of the results
        for amount_in in amounts_in:
            # We print with the decimal form.
            # WETH have 18 decimals so we put 18 for the decimal form.
            print(f"In {amount_in.exchange} you will need {blockchain_apis.get_token_decimal_form(amount_in.amountIn, 18)} WETH in order to get 2000.00 USDC")


asyncio.run(get_amount_in())
