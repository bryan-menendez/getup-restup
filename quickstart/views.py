from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics
from .serializers import UserSerializer, GroupSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """api that allows users to be viewed or modified"""
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """api that allows groups to be viewed or modified"""
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
