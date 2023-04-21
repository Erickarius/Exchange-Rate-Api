# Exchange Rate API

This is a simple Flask API that provides exchange rate information using data from the NBP API. It supports the following endpoints:

- `/exchanges/<currency_code>/<date>`: Returns the exchange rate for a specific currency and date.
- `/exchanges/<currency_code>/min-max/<int:n>`: Returns the minimum and maximum exchange rates for a specific currency over the last n days.
- `/exchanges/<currency_code>/diff/<int:n>`: Returns the maximum difference between the buy and ask rates for a specific currency over the last n days.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask (`pip install Flask`)
- requests (`pip install requests`)

### Installation

Clone the repository:

`bash:
git clone https://github.com/Erickarius/Exchange-Rate-Api.git
cd exchange-rate-api`

Install the required packages:

`bash:
pip install -r requirements.txt`

### Usage

To start the server, run the following command:

`cmd:
python app.py`

This will start the server on port 5000.

To test the API, you can use curl or any HTTP client of your choice. For example:

`bash:
curl http://localhost:5000/exchanges/EUR/2022-04-21`

This will return the exchange rate for USD on January 1st, 2022.
