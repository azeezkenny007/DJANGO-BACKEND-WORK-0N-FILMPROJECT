from .models import Snippet
from rest_framework.serializers import ModelSerializer


class SnippetSerializer(ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']