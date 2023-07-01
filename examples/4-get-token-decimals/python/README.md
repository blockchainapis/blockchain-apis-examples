# How to get the decimal of a token in Python

Find two examples of code that will give you the decimal of a token in the ethereum blockchain.

We advise you to use the [async](get_decimals.py) version of the code for
better performance.

If you already have a Python project and you don't want to bother with
async Python, you can use the [sync](get_decimals_sync.py) version.

## To run the example

### Install the dependencies:

```python
pip install -r requirements.txt
```

### Run any of the two instances:

_Sync:_
```bash
python get_decimals_sync.py
```

_Async:_
```bash
python get_decimals.py
```

## Example result

```
Token at address 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2 have 18 decimals.
```
