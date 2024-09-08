# Stress Testing Tool

This tool is designed to perform stress testing on a specified URL by sending a large number of requests and analyzing the results.

## Requirements

- [uv Package Manager](https://docs.astral.sh/uv/)
- Python 3.x
- Required Python packages (can be installed via `requirements.txt` if available)

## Installation

To install the required packages, including UV, follow these steps:

1. Install UV by following the instructions from the [official UV documentation](https://docs.astral.sh/uv/guides/install-python/):

For macOS and Linux:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Install other required Python packages:

```sh
pip install -r requirements.txt
```

## Usage

To use the stress testing tool, run the `stresser.py` script with the following command-line arguments:

- `--url`: The URL of the server to be tested (default: `http://your-apache-server.com/your-php-script.php`)
- `--requests`: The number of requests to send (default: `1000`)
- `--users`: The number of concurrent users (default: `50`)

### Example

```sh
python stresser.py --url http://example.com/test --requests 2000 --users 100
```
