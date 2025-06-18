import requests
endpoint="http://localhost:8000/api/products/"
data={
    "title":"Kasak saxena"
}
get_request=requests.get(endpoint,json=data)
print(get_request.json())
