from rest_framework import generics ,mixins,permissions,authentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin
from .permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    authentication_classes=[TokenAuthentication,authentication.SessionAuthentication]
    permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_create(self,serializer):
        #serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')or None 
        if content is None:
            content=title
        
        serializer.save(content=content)
    #send a django signal

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
   
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    permission_classes=[permissions.DjangoModelPermissions]
    
    
    def perform_update(self, serializer):
        instance= serializer.save()
        if not instance.content:
            instance.content=instance.title
            
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        

class ProductMixinView(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field="pk"
    
    def get(self,request,*args, **kwargs):
        print(args,kwargs)
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
      return self.create(request,*args, **kwargs)    

@api_view(["GET","POST"])
def product_alt_view(request,pk=None,*args, **kwargs):
    method = request.method 
    
    if method == "GET":
        if pk is not None:
            #detailview
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
        
        #List view
        queryset= Product.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)
    
    if method=="POST":
    #create an item
        
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content')or None 
            if content is None:
              content=title
        
            serializer.save(content=content)
            
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)
            