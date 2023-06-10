# How to get ethereum price?

In this example, you will find a way to get the ethereum price accross all of the
exchanges in multiple languages.

Find the full totorial here: https://docs.blockchainapis.io/docs/tutorial/getting-started/

### Example response

You will get a response like this:

amountOut is the amount of ETH that you will get after selling 1 ETH.

For example, in dooar_ethereum, we will get: 1706859077 USDC.

USDC has 6 decimals, so we with decimals, we will get:
1706.859077 USDC after selling 1.0 ETH on dooar ethereum.

```json
[
  {
    "blockchain": "ethereum",
    "exchange": "dooar_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "amountIn": 1000000000000000000,
    "amountOut": 1706859077
  },
  {
    "blockchain": "ethereum",
    "exchange": "elk_finance_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "amountIn": 1000000000000000000,
    "amountOut": 210231391
  },
  {
    "blockchain": "ethereum",
    "exchange": "pancakeswap_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "amountIn": 1000000000000000000,
    "amountOut": 1714461697
  },
  {
    "blockchain": "ethereum",
    "exchange": "plasmafinance_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "amountIn": 1000000000000000000,
    "amountOut": 87865886
  },
  {
    "blockchain": "ethereum",
    "exchange": "shibaswap_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "amountIn": 1000000000000000000,
    "amountOut": 1720572189
  },
  {
    "blockchain": "ethereum",
    "exchange": "sushiswap_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "amountIn": 1000000000000000000,
    "amountOut": 1733777461
  },
  {
    "blockchain": "ethereum",
    "exchange": "uniswapv2_ethereum",
    "tokenIn": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "tokenOut": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    "amountIn": 1000000000000000000,
    "amountOut": 1738214915
  }
]
```
