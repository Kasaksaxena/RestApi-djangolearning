from rest_framework import serializers 
from .models import Product 
from rest_framework.reverse import reverse
from .validation import validate_title

class ProductSerializer(serializers.ModelSerializer):
  my_discount=serializers.SerializerMethodField(read_only=True)
  editurl=serializers.SerializerMethodField(read_only=True)  
  url=serializers.HyperlinkedIdentityField(
      view_name='product-detail',lookup_field='pk')
  title=serializers.CharField(validators=[validate_title])                                         
#   email=serializers.EmailField(write_only=True)
  class Meta:
      model= Product
      fields=[
          'url',
          'editurl',
        #   'email',
          'pk',
          'title',
          'content',
          'price',
          'sale_price',
          'my_discount',
      ]
  # def validate_title(self,value):
  #   qs=Product.objects.filter(title__iexact=value)
  #   if qs.exists():
  #     raise serializers.ValidationError(f"{value} is already a product")
  #   return value
#   def create(self,validated_data):
#       #email=validated_data.pop('email')
#       obj=super().create(validated_data)
#       #print(email,obj)
#       return obj
#   def update(self,instance,validated_data):
#       ##instance.title=validated_data.get("title")
#       email=validated_data.pop('email')
#       return super().update(instance,validated_data)
#       ##return instance
  
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
    
   