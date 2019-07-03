from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Card,Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id','User','Product','VoucherNum','CardPin','IsArchived')

    