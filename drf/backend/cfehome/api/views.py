import json
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder

#api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response

#serializer
from products.serializers import ProductSerializer
# Create your views here.

@api_view(["GET"])
def api_home(request,*args, **kwargs):
    """ 
    DRF API VIEW
    """
    #if request.method=="POST":
        #return Response({"detail": "GET not Allowed"},status=405)
    instance=Product.objects.all().order_by("?").first()   
    data={}
    if instance: 
        data=ProductSerializer(instance).data
        #data=model_to_dict(instance, fields=['id','title',"price"])
        return Response(data)
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