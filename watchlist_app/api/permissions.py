from rest_framework import permissions 
#from rest_framework.permissions import BasePermission, SAFE_METHODS 
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

class IsAdminOrReadOnly(IsAdminUser): 
    
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission        
    
"""class AdminOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        # Allow read-only methods for everyone
        if request.method in SAFE_METHODS:
            return True

        # Allow write permissions only to admin users
        return bool(request.user and request.user.is_staff)   """
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            #check permission for readonly 
        else:
            # check permissions for write request
            return obj.review_user == request.user 
                