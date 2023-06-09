from django.shortcuts import render
from rest_framework import status
from .models import Candidate, Position
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
# # Create your views here.


class VoteView(APIView):
    def post(self, request):
        name = request.data["name"]
        if name:
            try:
                candidate = Candidate.objects.get(name__iexact=name)
                print(candidate, "🧓🏿")
                candidate.votes += 1
                candidate.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Candidate.DoesNotExist:
                return Response({"error": "Candidate not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "No name was provided"}, status=status.HTTP_400_BAD_REQUEST)




   