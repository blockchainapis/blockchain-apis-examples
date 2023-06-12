# How to handle Blockchain APIs Exceptions in Python

The main instance of Blockchain APIs may throw some exceptions.

These exceptions can happen only in the following cases:
- An invalid parameter is put inside of a request
- You make more request than allowed by your API key (will throw a [TooManyRequestsException](https://docs.blockchainapis.io/docs/python-sdk/exceptions/too-many-requests-exception))
- Your API key is expired or not invalid. In this case, an [UnauthorizedException](https://docs.blockchainapis.io/docs/python-sdk/exceptions/unauthorized-exception) is thrown.

## To run the example

### Install the dependencies:

```python
pip install -r requirements.txt
```

### Run any of the two instances:

_Sync:_
```bash
python catch_exceptions_sync.py
```

_Async:_
```bash
python catch_exceptions.py
```

_Do not hesitate to play with the examples and modify them to create your Proof of Concept_
