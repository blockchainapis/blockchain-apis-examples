# How to get the decimals of a token?

Inside of the blockchains, all values are stored as integers.

But in interfaces that interact with the blockchain like [Uniswap](https://app.uniswap.org/#/swap),
you see the token values in decimal form and not integers.

That is because the [ERC20 token standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) have
a `decimal` variable that shows with how many decimal places that token should be displayed to the end user.

In this example, you will find out how to use [BlockchainAPIs](https://www.blockchainapis.io) in order to get
the decimal of a token.
