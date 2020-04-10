# SolidGate API
This library provides basic API options of SolidGate payment gateway.

## Requirements

- Python 3.7
- Packages: requests

## Installation

Use pip command: ```pip install solidgate-card-sdk```

## Usage

Create a class instance of the 'ApiClient' class.
```
from solidgate-card-sdk import api_client

client = api_client.ApiClient(merchant_id, private_key)
```
- merchant_id - unique merchant identification;
- private_key - secret code for request signature. It's provided at the moment of merchant registration.

## Documentation
* https://solidgate.atlassian.net/wiki/spaces/API/overview

## Support
If you have any problems, questions or suggestions send your inquiry to info@solidgate.com.