from blockchainapis import BlockchainAPIsSync

blockchain_apis = BlockchainAPIsSync()

amount_out = blockchain_apis.amount_out(
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

print(amount_out)
