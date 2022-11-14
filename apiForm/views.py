from apiForm.serializers import UserSerializer
from rest_framework import viewsets, permissions
from apiForm.models import User


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]
