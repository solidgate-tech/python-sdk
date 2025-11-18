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
* **Solidgate account**: Public and secret key (request via <a href="mailto:sales@solidgate.com">sales@solidgate.com</a>)

<br>

## Installation

To start using the Python SDK:

1. Ensure you have your public and secret key.
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

---

<div style="display: flex; flex-direction: column; gap: 3px; max-width: 400px;">
  <div style="display: flex; align-items: center; gap: 5px;">
    <svg width="15" height="15" viewBox="0 -1 24 24" xmlns="http://www.w3.org/2000/svg">        <path d="M3 3h18v12H6l-3 3V3z" stroke="#808080" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <span style="font-size: 14px;">Looking for help? <a href="https://support.solidgate.com/support/tickets/new" target="_blank">Contact us</a></span>
  </div>
  <div style="display: flex; align-items: center; gap: 5px;">
    <svg width="15" height="12" viewBox="0 1 21 19" xmlns="http://www.w3.org/2000/svg">
      <path d="M1 12L4.5 15.5L14 6" stroke="#808080" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M6 13L9.5 16.5L19 7" stroke="#000000" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    <span style="font-size: 14px;">Want to contribute? <a href="https://github.com/solidgate-tech/python-sdk/pulls" target="_blank">Submit a pull request</a></span>
  </div>
</div>
