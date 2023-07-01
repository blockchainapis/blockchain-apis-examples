from blockchainapis import BlockchainAPIsSync

# Create the blockchain APIs instance to interact with Blockchain APIs
# You can also optionally get an API key at:
# https://dashboard.blockchainapis.io
# An create the instance this way:
# blockchain_apis = BlockchainAPIsSync(api_key)
blockchain_apis = BlockchainAPIsSync()

# The id of the blockchain that you want to get the decimals from.
#
# If you want to get the list of valid blockchain ids, you can follow this tutorial:
# https://docs.blockchainapis.io/docs/tutorial/getting-started/get-supported-blockchains
BLOCKCHAIN = "ethereum"

# The token that you want to get the decimals from
# Here: 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2, is the address of the WETH
# token.
TARGET_TOKEN = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

# Make a call to Blockchain APIs in order to get the decimals.
decimals = blockchain_apis.decimals(blockchain=BLOCKCHAIN, token=TARGET_TOKEN)

print(f"Token at address {TARGET_TOKEN} have {decimals} decimals.")
