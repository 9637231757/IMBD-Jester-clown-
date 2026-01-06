#from django.shortcuts import render
from rest_framework.decorators import api_view 
#from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user_app.api.serializers import RegistrationSerializer 
from rest_framework.authtoken.models import Token 
from rest_framework import status
from user_app import models


# Create your views here below.

@api_view(['POST',])
def logout_view(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status.HTTP_200_OK)

        
@api_view(['POST',])
def registration_view(request):        
    
    if request.method == 'POST':
         serializer = RegistrationSerializer(data=request.data)
         
         data = {}
         
         if serializer.is_valid():
             account = serializer.save() 
             
             data['response'] = "Registration Sucessful!"
             data['username'] = account.username 
             data['email'] = account.email 
             
             #token = Token.objects.get_or_create(user=account).key 
             #data['token'] = token 
             
             
             token, created = Token.objects.get_or_create(user=account)
             data['token'] = token.key

         else: 
             data = serializer.errors
                 
         return Response(data) 
         
    
        
    
    

     