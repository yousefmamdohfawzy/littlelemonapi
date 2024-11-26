from rest_framework import serializers
from .models import MenuItem , Cart,Order, OrderItem
from rest_framework.response        import Response
from django.contrib.auth.models     import Group, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']                
                  
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','category','featured']
    
    
    
class singleMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','category','featured']


class CartSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source='user.username')
    menuitem=serializers.StringRelatedField()# return the menu item title
    class Meta:
        model= Cart
        fields=['user','username','menuitem','quantity','unit_price','price']
    

class OrderItemSerializer(serializers.ModelSerializer):
    order_id=serializers.CharField(source='order.id',read_only=True)
    menuitem = serializers.CharField(source='menuitem.title', read_only=True)
    menuitem_Id= serializers.CharField(source='menuitem.id', read_only=True)
    class Meta:
        model=OrderItem
        fields=['order_id','menuitem','menuitem_Id','quantity','unit_price','price']

class OrderSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField(source='delivery_crew', read_only=True)
    items= OrderItemSerializer(many=True,read_only=True)
    order_status = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'assigned_to', 'order_status', 'items']

    def get_order_status(self,obj):
        if obj.status ==1:
            return ("Delivered")
        else:
            return('Delivery in Progress')
        