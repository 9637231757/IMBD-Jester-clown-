from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import registration_view, logout_view
 
urlpatterns = [
    
    #path('admin/', admin.site.urls),
    #path('login/', obtain_auth_token, name='login'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/',registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    #path('api/token/', obtain_auth_token),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]