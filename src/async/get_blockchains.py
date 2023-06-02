import asyncio

from blockchainapis import BlockchainAPIs

async def get_blockchains():
    """
    Get the list of available blockchains using the API
    
    With the output result, you can get the id of the blockchain
    that can be later used during other API calls
    """
    blockchain_apis = BlockchainAPIs()
    blockchains = await blockchain_apis.blockchains()

    # Print all of the blockchains available
    print(blockchains)
    # Print the id of all of the blockchains available
    print("", *[blockchain.blockchain for blockchain in blockchains], sep='\n- ')
    await blockchain_apis.close()

asyncio.run(get_blockchains())
