#!/user/bin/env python

import requests

print requests.__version__

response = requests.get("https://raw.githubusercontent.com/AaronHongyangLiu/c404LAB/master/script.py")

print response.text
print response.staus_code
