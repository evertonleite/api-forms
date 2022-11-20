from rest_framework import serializers
from apiForm.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'id',
      'name',
      'email',
      'password',
      'type_user'
    ]