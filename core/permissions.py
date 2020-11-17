from rest_framework import permissions


class IsPostOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        # todo, add leaky bucket rate limiter by ip
        if request.method == 'POST':
            return True

        return bool(request.user and request.user.is_authenticated)
