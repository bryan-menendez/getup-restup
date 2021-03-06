from django.contrib.auth.models import User, Group
from rest_framework import serializers
from snippets.models import Snippet


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'groups', 'snippets']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']