from pipes import Template
from re import template
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic.detail import DetailView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
        


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class HomeView(APIView):

    def get(self, request, format=None):
        return Response("VIEW")

class SingleUserViewSet(DetailView):
    # queryset = User.objects.get()
    # serializer_class = UserSerializer
    # template_name = "/templates/singleUserTemplate.html"

    model = User
    template_name = "templates/singleUserTemplate.html"

    def get_context_data(self, id):
        context = super().get_context_data(id)
        render(self, context, template_name="templates/singleUserTemplate.html")