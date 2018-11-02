import requests
import time

endpoint = "https://sitename.azurewebsites.net"

for i in range(0, 10):
    t0 = time.time()
    r = requests.get(endpoint)
    t1 = time.time()
    print(str(r.status_code) + " in " + str(t1-t0) + "ms")
