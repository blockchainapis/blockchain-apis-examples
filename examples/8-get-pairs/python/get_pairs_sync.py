from blockchainapis import BlockchainAPIsSync

blockchain_apis = BlockchainAPIsSync()
# You can also get an API key at:
# https://dashboard.blockchainapis.io
# An create the instance this way:
# blockchain_apis = BlockchainAPIsSync(api_key)

# Get pairs for every blockchain
pairs = blockchain_apis.pairs()
# TIP: You can specify a specific blockchain id by doing the folowing:
# pairs = blockchain_apis.pairs(blockchain="ethereum")

# There are 100 results per page by default we start at page 1
print(f"Current page: {pairs.page}")
# We print the total amount of pages:
print(f"Total pages: {pairs.total_pages}")
# TIP: You can choose which page you want to get by doing the following:
# pairs = await blockchain_apis.pairs(page=2)

# Now we get the first pair available:
pair = pairs.data[0]
print("First pair:")
# The id of the blockchain on which the pair is
print(f"Blockchain ID of pair: {pair.blockchain}")
# The id of the exchange on which the pair is
print(f"Exchange ID of pair: {pair.exchange}")
# A pair contains two tokens: token0 and token1
# In order to be able to execute a trade in any of these pairs, you will need
# to own some token0 or token1.
print(f"Token0 of pair: {pair.token0}")
print(f"Token1 of pair: {pair.token1}")
# The fee taken by liquidity providers during a trade
# The fee is written in 100000 of percents (for example: 1000 is 1%)
print(f"fee: {pair.fee}")
