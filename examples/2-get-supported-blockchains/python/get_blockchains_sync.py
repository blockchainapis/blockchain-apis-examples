from blockchainapis import BlockchainAPIsSync

blockchain_apis = BlockchainAPIsSync()
# You can also get an API key at:
# https://dashboard.blockchainapis.io
# An create the instance this way:
# blockchain_apis = BlockchainAPIsSync(api_key)

# Make an API call in order to get the list of blockchains.
blockchains = blockchain_apis.blockchains()

# print("=======================")
# The returned result is a list, so we need to loop throught the result
for blockchain in blockchains:
    print(f"- {blockchain.blockchain}")
    # Print the name of the blockchain
    # print(f"Blockchain name: {blockchain.name}")
    # Print the id of the blockchain:
    # print(f"Blockchain id: {blockchain.blockchain}")
    # Print the chain id
    # print(f"Chain id: {blockchain.chain_id}")
    # Print the url to the explorer of the blockchain:
    # print(f"Blockchain explorer: {blockchain.explorer}")
    # print("=======================")
