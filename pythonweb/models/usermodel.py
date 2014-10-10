from django.db import models
from rest_framework import serializers

class UserModel(models.Model):
    firstName = models.CharField(default='Timbo', max_length=512)
    lastName = models.CharField(default='Walker', max_length=512)

    def serialize(self):
        serializer = UserSerializer(self)
        return serializer.data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('firstName', 'lastName')