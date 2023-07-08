# How to display a token in his decimal form

Inside of the blockchains, all values are stored as integers.

But in interfaces that interact with the blockchain like [Uniswap](https://app.uniswap.org/#/swap),
you see the token values in decimal form and not integers.

That is because the [ERC20 token standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) have
a `decimal` variable that shows with how many decimal places that token should be displayed to the end user.

In this example, you will find out how to use [BlockchainAPIs](https://www.blockchainapis.io) in order to display a certain integer amount of tokens into his decimal form, and the reverse also.

For these examples, we will use the Wrapped ETH token: `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`, and the USDC token: `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`

We will convert: `2450000000000000000 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2` into his decimal form: `2.45 WETH`

And we will convert: `2542.42 USDC` to his integer form: `2542420000 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`
