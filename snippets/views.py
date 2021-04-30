from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework import mixins, generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
