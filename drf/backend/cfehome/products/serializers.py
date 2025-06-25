from rest_framework import serializers 
from .models import Product 
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
  my_discount=serializers.SerializerMethodField(read_only=True)
  editurl=serializers.SerializerMethodField(read_only=True)  
  url=serializers.HyperlinkedIdentityField(
      view_name='product-detail',lookup_field='pk'
                                            )
  
  class Meta:
      model= Product
      fields=[
          'url',
          'editurl',
          'pk',
          'title',
          'content',
          'price',
          'sale_price',
          'my_discount',
      ]
  def get_editurl(self,obj):
       #return f"/api/products/{obj.pk}/" 
       request=self.context.get('request')
       if request is None:
           return None
       return reverse("product-update",kwargs={"pk":obj.pk},request=request)
  def get_my_discount(self,obj):
    if not hasattr(obj,'id'):
        return None
    if not isinstance(obj,Product):
        return None
        
    return obj.get_discount()      
    
   