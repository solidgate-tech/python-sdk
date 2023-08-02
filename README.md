[![PyPI version](https://badge.fury.io/py/solidgate-sdk.svg)](https://badge.fury.io/py/solidgate-sdk)

# SolidGate API
This library provides basic API options of SolidGate payment gateway.

## Requirements

- Python 3.7
- Packages: requests
- SolidGate account. If you don’t have this you can request it by contacting sales@solidgate.com

## Installation

Use pip command: ```pip3 install solidgate-card-sdk```

## Usage

Create a class instance of the 'ApiClient' class.
```
from solidgate import ApiClient

client = ApiClient(public_key, secret_key)
```
- public_key - unique merchant identification;
- secret_key - secret code for request signature. It's provided at the moment of merchant registration.

## Documentation
* https://docs.solidgate.com

## Support
If you have any problems, questions or suggestions send your inquiry to info@solidgate.com.
