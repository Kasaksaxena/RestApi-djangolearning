import requests
# endpoint is webaddress(url) u call to get specific data from an api
#endpoint= "https://httpbin.org/status/200/"
#endpoint="https://httpbin.org/anything"
endpoint="http://localhost:8000/api/"
#get_request=requests.get(endpoint, params={"abc": 123}, json={"query":"Hello World!"})
#print(get_request.json()["message"])
#print(get_request.text)
get_request=requests.get(endpoint)
print(get_request.json())

#print(get_request.status_code)

