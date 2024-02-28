import requests

coindesk_url = 'https://claraj.github.io/mock-bitcoin/currentprice.json'


def main():
    bitcoin = get_bitcoin_amount()
    dollars = convert_bitcoin_to_dollars(bitcoin)
    display_results(bitcoin, dollars)


def get_bitcoin_amount():
    while True:
        try:
            bitcoin = float(input('Enter the number of bitcoin: '))
            if bitcoin >= 0:
                return bitcoin
            else:
                print(' Please enter a number greater than 0')
        except ValueError:
            print('Enter a positive number.')


def get_rate_json():  # mocked function
    response = requests.get(coindesk_url)
    data = response.json()
    return data


def extract_rate(rate_json):
    dollars_exchange_rate = rate_json['bpi']['USD']['rate_float']
    return dollars_exchange_rate


def convert_bitcoin_to_dollars(bitcoin):
    exchange_rate_json = get_rate_json()
    dollars_exchange_rate = extract_rate(exchange_rate_json)
    bitcoin_value_in_dollars = bitcoin * dollars_exchange_rate
    return bitcoin_value_in_dollars


def display_results(bitcoin, dollars):
    print(f'{bitcoin} bitcoin is equal to ${dollars:,.2f} US Dollars')


if __name__ == '__main__':
    main()