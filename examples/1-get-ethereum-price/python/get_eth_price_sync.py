from blockchainapis import BlockchainAPIsSync

blockchain_apis = BlockchainAPIsSync()
# You can also get an API key at:
# https://dashboard.blockchainapis.io
# An create the instance this way:
# blockchain_apis = BlockchainAPIsSync(api_key)

# Do an API call in order to get the amount out
amount_outs = blockchain_apis.amount_out(
    # The blockchain on which you want the exchange to take place
    blockchain="ethereum",
    # The address of the token that we sell, here it is WETH address
    tokenIn="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    # The address of the token that we buy, here it is USDC
    tokenOut="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    # The amount of tokenIn that we sell.
    # Here we sell 1 WETH.
    # We need to add 10**18 because WETH have 18 decimals.
    amountIn=1 * 10**18
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
