# Solidgate API

[![PyPI version](https://badge.fury.io/py/solidgate-sdk.svg)](https://badge.fury.io/py/solidgate-sdk)

Python SDK provides API options for integrating Solidgate’s payment orchestrator into your Python applications.

Check our
* <a href="https://docs.solidgate.com/" target="_blank">Payment guide</a> to understand business value better
* <a href="https://api-docs.solidgate.com/" target="_blank">API Reference</a> to find more examples of usage

## Structure

<table style="width: 100%; background: transparent;">
  <colgroup>
    <col style="width: 50%;">
    <col style="width: 50%;">
  </colgroup>
  <tr>
    <th>SDK for Python contains</th>
    <th>Table of contents</th>
  </tr>
  <tr>
    <td>
      <ul>
        <li>
          <code>solidgate/</code> – main library source code for development
          <ul>
            <li><code>__init__.py</code> – initializes the SDK package for importing</li>
            <li><code>api_client.py</code> – main file for API integration and HTTP request handling</li>
            <li><code>encryption.py</code> – library for encryption-related operations</li>
            <li><code>model.py</code> – defines data structures for payment attributes and responses</li>
          </ul>
        </li>
        <li><code>setup.py</code> – script for managing dependencies and library imports</li>
      </ul>
    </td>
    <td>
        <a href="https://github.com/solidgate-tech/python-sdk?tab=readme-ov-file#requirements">Requirements</a><br>
        <a href="https://github.com/solidgate-tech/python-sdk?tab=readme-ov-file#installation">Installation</a><br>
        <a href="https://github.com/solidgate-tech/python-sdk?tab=readme-ov-file#usage">Usage</a><br>
        <a href="https://github.com/solidgate-tech/python-sdk?tab=readme-ov-file#errors">Errors</a><br>
    </td>
  </tr>
</table>

<br>

## Requirements

* **Python**: 3.7 or later
* **Packages**: `requests` library
* **Solidgate account**: Merchant ID and secret key (request via <a href="mailto:sales@solidgate.com">sales@solidgate.com</a>)

<br>

## Installation

To start using the Python SDK:

1. Ensure you have your merchant ID and secret key.
2. Install the SDK in your project using pip:
   ```bash
   pip install solidgate-card-sdk
   ```
3. Import the classes into your project:
    ```
   from solidgate import ApiClient
   client = ApiClient(public_key='YourMerchantId', secret_key='YourPrivateKey')
   ```
4. Use test credentials for integration testing. After successful testing, switch to production credentials.

<br>

## Usage

### Charge a payment

Create a class instance of the `ApiClient` class.

```
from solidgate import ApiClient

client = ApiClient(public_key, secret_key)
```

- `public_key` - unique merchant identification
- `secret_key` - secret code for request signature, it is provided at the moment of merchant registration

### Resign form

```python
response = client.form_resign({'order_id': '12345'})
```

<br>

## Errors

Handle <a href="https://docs.solidgate.com/payments/payments-insights/error-codes/" target="_blank">errors</a>.

```python
try:
    response = client.charge({...})
except Exception as e:
    print(e)
```
