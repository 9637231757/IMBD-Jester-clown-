from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    #path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name='login'),
    #path('api/token/', obtain_auth_token),

    
 
]
