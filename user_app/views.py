#from django.shortcuts import render
from rest_framework.decorators import api_view 

from user_app.api.serializers import RegestrationSerializer  


# Create your views here.
@api_view(['POST', ])
def registration_view(request):
    
    if request.method == 'POST':
         serializer = RegestrationSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save() 
             return serializer.data 
         
    
        
    
    

     