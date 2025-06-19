import requests
headers={'Authorization':'Bearer ee0a1c5c43a572b33c1bb6803af51f9820a4d970'}
endpoint="http://localhost:8000/api/products/"
data={
    "title":"Kasak saxena"
}
get_request=requests.post(endpoint,json=data,headers=headers)
print(get_request.json())
