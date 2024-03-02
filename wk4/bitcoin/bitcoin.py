import requests
import sys

# Requires that the user give a second command-line argument that is also a floating integer, as Bitcoin shares

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        print('Number required for command-line argument')
        sys.exit(1)
else:
    print('Missing command-line argument')
    sys.exit(1)

# Requests Bitcoin info from the web and then calculates the value of the shares of Bitcoin that was entered in the command-line

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    value = r.json()['bpi']['USD']['rate_float'] * float(sys.argv[1])
    print(f'Value: ${value:,.4f}')
except requests.RequestException:
    print('Request Exception')
    sys.exit(1)