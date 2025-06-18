import requests
endpoint="http://localhost:8000/api/products/1/"
get_request=requests.get(endpoint)
print(get_request.json())
