from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app import models
from rest_framework import generics

@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class Registration(generics.CreateAPIView):
    serializer_class = RegistrationSerializer  

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):

        serializer = RegistrationSerializer(data=self.request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token
            print(f"Token is {token}")
        
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Suceessful!"
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token
        
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)
