from blockchainapis import BlockchainAPIsSync

blockchain_apis = BlockchainAPIsSync()
# You can also get an API key at:
# https://dashboard.blockchainapis.io
# An create the instance this way:
# blockchain_apis = BlockchainAPIsSync(api_key)

blockchains = blockchain_apis.blockchains()
