from rest_framework import serializers
from .models import Candidate,Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name')

class CandidateSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)
    class Meta:
        model = Candidate
        fields = ('id', 'name', 'position', 'votes')
