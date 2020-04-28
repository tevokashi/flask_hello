import requests
import sys

url =  'cpro43392.publiccloud.com.br:31500/api/v1/status'
req = requests.get("http://{}".format(url)).json()
if float(req.get('API').get('api')) == 1.0:
    print('OK')
    print(req)
else:
    print('ned rolback')
    sys.exit(4)
