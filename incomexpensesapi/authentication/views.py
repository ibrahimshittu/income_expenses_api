from django.shortcuts import render
from rest_framework import generics, status
from .serializers import registerSerializer
from rest_framework.response import Response

# Create your views here.


class registerView(generics.GenericAPIView):

    serializer_class = registerSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_200_OK)
