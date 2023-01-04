"""dom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',snippet_list,name="snippets"),
    path('<int:pk>',snippet_detail,name="snippetsDetails"),
    path('a',Attend,name="attend"),
    path('p',SnippetList.as_view(),name="attend"),
    path('p<int:pk>',SnippetDetail.as_view(),name="attend"), 
    path('t/',TodoGetAndPost.as_view(),name="GetPost"), 
    path('t<int:pk>',SnippetDetail.as_view(),name="attend"), 
]


urlpatterns = format_suffix_patterns(urlpatterns)