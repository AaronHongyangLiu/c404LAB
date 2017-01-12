#!/user/bin/env python

import requests

print requests.__version__

response = requests.get("http://google.com/")

print response.text
print response.staus_code
