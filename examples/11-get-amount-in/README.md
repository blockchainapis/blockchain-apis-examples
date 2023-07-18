# How to get the amount in of tokens required in order to buy a token?

[Blockchain APIs](https://www.blockchainapis.io) allow you to get the amount of
tokens that you will need in order to get a certain amount of tokens.

In this example, we will get the amount of ETH that is required in order to get
2000 USDC on the Ethereum blockchain.

Running the example should give you this output:

```
In dooar_ethereum you will need 1.071419893150198561 WETH in order to get 2000.00 USDC
In elk_finance_ethereum you will need 0 WETH in order to get 2000.00 USDC
In pancakeswap_ethereum you will need 1.073992537197660008 WETH in order to get 2000.00 USDC
In plasmafinance_ethereum you will need 0 WETH in order to get 2000.00 USDC
In shibaswap_ethereum you will need 1.071930904276886242 WETH in order to get 2000.00 USDC
In sushiswap_ethereum you will need 1.059925181087655307 WETH in order to get 2000.00 USDC
In uniswapv2_ethereum you will need 1.059933556462899155 WETH in order to get 2000.00 USDC
```

Please note that if you see "0", it means that there is not enough liquidity on the exchange
in order to make the trade.
