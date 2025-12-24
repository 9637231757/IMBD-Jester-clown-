
from django.contrib import admin
from django.urls import path, include
#from user_app.api.views import logout_view   


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Watch/', include('watchlist_app.api.urls')),
    path('account/', include('user_app.api.urls')),
    path('api-auth', include('rest_framework.urls')),
    
    #path('api-auth/', include('rest_framework.urls')),


]
