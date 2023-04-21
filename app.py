from datetime import datetime
from flask import Flask, jsonify, abort
import requests

app = Flask(__name__)

@app.route('/exchanges/<currency_code>/<string:date>')
def get_exchange_rate(currency_code, date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        abort(400, 'Invalid date format. Please use YYYY-MM-DD.')
    
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{date}/'
    response = requests.get(url)

    if response.status_code == 404:
        abort(404, 'Exchange rate not found')

    data = response.json()
    rate = data['rates'][0]['mid']

    return jsonify({'rate': rate})

@app.route('/exchanges/<currency_code>/min-max/<int:n>')
def get_min_max_average(currency_code, n):
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/last/{n}/'
    response = requests.get(url)

    if response.status_code == 404:
        abort(404, 'Exchange rates not found')

    data = response.json()
    rates = [d['mid'] for d in data['rates']]
    min_rate = min(rates)
    max_rate = max(rates)

    return jsonify({'min_rate': min_rate, 'max_rate': max_rate})

@app.route('/exchanges/<currency_code>/diff/<int:n>')
def get_diff(currency_code, n):
    url = f'http://api.nbp.pl/api/exchangerates/rates/c/{currency_code}/last/{n}/'
    response = requests.get(url)

    if response.status_code == 404:
        abort(404, 'Exchange rates not found')

    data = response.json()
    rates = [(d['bid'] - d['ask']) for d in data['rates']]
    max_diff = max(rates)

    return jsonify({'max_diff': max_diff})

if __name__ == '__main__':
    app.run()
