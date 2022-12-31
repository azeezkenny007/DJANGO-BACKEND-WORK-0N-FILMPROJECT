from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import *

from django.views.decorators.csrf import csrf_exempt
# This is used to make an HTTP Post request which can be consumed with axios
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
# This converts our data from the models to any type of data needed
from snippets.serializers import SnippetSerializer
# This replaces the statically typed error or success statically type handlers 
from rest_framework import status
# The import help to ensure concise usage of the api_view
from rest_framework.decorators import api_view
# This import is an extension of the HTTPResponse , but it allows to define in a way that is wanted
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST'])
def snippet_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
       
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def Attend(request):
    attendance = Attendance.objects.filter(student__name="azeez")
    print(attendance)
    data = serializers.serialize()

   