from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import registration_view
 
urlpatterns = [
    
    #path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name='login'),
    path('regester/',regestration_view, name='regester'),
    #path('api/token/', obtain_auth_token),

    
 
]
