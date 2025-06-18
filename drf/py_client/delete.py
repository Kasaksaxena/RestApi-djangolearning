import requests

product_id=input("What is your id you want to use?\n")
try:
    product_id=int(product_id)
    
except:
    product_id=None
    print(f"{product_id}is not valid")
    
if product_id:
    endpoint=f"http://localhost:8000/api/products/{product_id}/delete/"        
get_request=requests.delete(endpoint)
print(get_request.status_code,get_request.status_code==204)
