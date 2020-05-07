import requests
import sys

url = 'cpro43392.publiccloud.com.br:31500/api/v1/status'
req = requests.get("http://{}".format(url)).json()
if float(req.get('API').get('api')) == 1.1:
    print('OK')
    print(req)
else:
    print('efetuando o rollback ?')
    print(req)
    sys.exit(4)
