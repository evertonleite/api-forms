from rest_framework import serializers
from apiForm.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    
    #outra forma com que pode escolher os campos para serializar
    #[
    #   'id',
    #   'name',
    #   'email',
    #   'password',
    #   'type_user'
    # ]