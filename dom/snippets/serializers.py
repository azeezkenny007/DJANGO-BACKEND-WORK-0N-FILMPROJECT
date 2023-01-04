from .models import Snippet,NameCategory,Todo
from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField,StringRelatedField


class SnippetSerializer(ModelSerializer): 
    class Meta:
        model = Snippet
        fields = "__all__"
        
class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields ="__all__"