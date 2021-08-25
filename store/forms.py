from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Require, Shop, Product, OrderItem, Ship

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'number', 'address', 'city', 'state', 'zipcode']

class RequireForm(ModelForm):
    class Meta:
        model = Require
        fields = ['customer', 'product', 'category', 'image', 'description']

class DealerForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'number', 'shop_identity', 'address', 'city', 'state', 'zipcode']

class ShipForm(ModelForm):
    class Meta:
        model = Ship
        fields = ['name', 'number', 'ship_identity', 'address', 'city', 'state', 'zipcode']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'description', 'shop', 'category']

class PackForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['packed', 'shipment']

class ShipStatusForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['shipped']

class ShipStatusForm2(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['out_for_delivery']

class ShipStatusForm3(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['delivered']
