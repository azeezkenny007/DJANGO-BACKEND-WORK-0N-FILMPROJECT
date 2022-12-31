from .models import Snippet,NameCategory
from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField,StringRelatedField


class SnippetSerializer(ModelSerializer): 
    class Meta:
        model = Snippet
        fields = "__all__"