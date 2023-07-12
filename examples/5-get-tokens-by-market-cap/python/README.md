# How to get the market cap of all tokens of a blockchain in Python

Find two examples of code that will give you the first 100 tokens that have the biggest
market cap inside of the Ethereum Blockchain.

We advise you to use the [async](get_tokens_market_cap.py) version of the code for
better performance.

If you already have a Python project and you don't want to bother with
async Python, you can use the [sync](get_tokens_market_cap_sync.py) version.

In our example, we will get the list and print the top 10 tokens.

Here is how the output should look like:
| Token Address                              | Blockchain ID   | Decimals | Market Cap               |
| ------------------------------------------ | --------------- | -------- | ------------------------ |
| 0xc6cd44F9630886a7492cEa3d9860e0510933A600 | ethereum        | 18       | 1.2803270158023658e+16   |
| 0x50243F43D40AeFE1dbC138EE9BBD5368AC9A47d8 | ethereum        | 18       | 567509874127901.1        |
| 0x872D63d889D4b445C89A0887dcdBCc179B026432 | ethereum        | 18       | 4507922029597.652        |
| 0xc0F4014A41C7511Bf22351a132A7282F84EaeC3a | ethereum        | 18       | 2401754872132.872        |
| 0x0240E59E6AE33b58DB7360f7c693429Eab7d4aC3 | ethereum        | 18       | 159925162980.2042        |
| 0x11E003e9eCC5a2320E8b11098ACd550b928b6df2 | ethereum        | 7        | 64876220860.16215        |
| 0x5052fa4a2a147eaAa4c0242e9Cc54a10A4f42070 | ethereum        | 18       | 43044039383.26699        |
| 0xdAC17F958D2ee523a2206206994597C13D831ec7 | ethereum        | 6        | 39028663976.21173        |
| 0xCc802c45B55581713cEcd1Eb17BE9Ab7fcCb0844 | ethereum        | 18       | 31809324779.483967       |
| 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 | ethereum        | 6        | 25521103384.255188       |

Please note some tokens have a weird market cap:
- 0xc6cd44F9630886a7492cEa3d9860e0510933A600
- 0x50243F43D40AeFE1dbC138EE9BBD5368AC9A47d8

This is because in order to compute the market cap, Blockchain APIs uses the following method:
1. Remove all tokens that have a liquidity lower than 25000 USDT
2. Compute the value of the token in USDT
3. Multiply this value by the total supply of tokens

So, as long as a token has more than 25000 USDT in his liquidity, we considere that it has a valid market
cap to compute.

## To run the example

### Install the dependencies:

```python
pip install -r requirements.txt
```

### Run any of the two instances:

_Sync:_
```bash
python get_tokens_market_cap_sync.py
```

_Async:_
```bash
python get_tokens_market_cap.py
```

## Example result


