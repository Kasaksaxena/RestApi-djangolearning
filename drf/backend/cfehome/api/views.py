import json
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
def api_home(request,*args, **kwargs):
    model_data=Product.objects.all().order_by("?").first()   
    data={}
    if model_data: 
        data=model_to_dict(model_data, fields=['id','title',"price"])
        return JsonResponse(data)
        # json_data_str=json.dumps(data, cls=DjangoJSONEncoder)

# """print(request.GET)
# body=request.body #byte string of json data
# data={}
# try:
# data=json.loads(body)
# except:
# pass
# print(data)  
# data['params']=dict(request.GET)
# print(request.headers)
# json.dumps(dict(request.headers))
# data["content_type"]=request.content_type
# """
  
  
    # return HttpResponse(json_data_str,headers= {"content-type": "application/json"})