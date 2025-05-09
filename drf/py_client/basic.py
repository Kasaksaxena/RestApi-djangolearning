import requests
# endpoint is webaddress(url) u call to get specific data from an api
endpoint= "https://httpbin.org/status/200/"
endpoint="https://httpbin.org/anything"
get_request=requests.get(endpoint)
print(get_request.json())
