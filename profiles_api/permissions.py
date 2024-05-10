from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        # Return True if the user is trying to edit their own profile
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
    

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their status only"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own status"""
        # Only allow authenticated users
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id
