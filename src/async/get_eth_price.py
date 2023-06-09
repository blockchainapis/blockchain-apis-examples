import asyncio

from blockchainapis import BlockchainAPIs

# The blockchain that you want to get the price from
BLOCKCHAIN = "ethereum"

# The address of the token that we are selling
# Here we put the address of wrapped ETH
TOKEN_IN = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

# The address of the token that we are buying
# Here we put USDT
TOKEN_OUT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

# The amount of TOKEN_IN that we are selling.
# We add 10**18 because the TOKEN_IN is WETH and WETH has
# 18 decimals
AMOUNT_IN = 1 * 10**18

async def get_price():
    blockchain_apis = BlockchainAPIs()
    amount_out = await blockchain_apis.amount_out(
        blockchain=BLOCKCHAIN,
        tokenIn=TOKEN_IN,
        tokenOut=TOKEN_OUT,
        amountIn=AMOUNT_IN
    )
    print(amount_out)
    await blockchain_apis.close()

asyncio.run(get_price())
