from django.contrib.auth.models import User
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer

class SnippetList(generics.ListCreateAPIView):
    model = Snippet
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Snippet
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer


class UserInstance(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
