import requests
endpoint="http://localhost:8000/api/products/1/update/"
data={
    "title":"Dileep kumar saxena",
    "price":"25.06"
    
}

get_request=requests.put(endpoint,json=data)
print(get_request.json())
