from django.urls import path

from core.views.category import CategoryViewSet
from core.views.note import NoteViewSet
from core.views.user import UserViewSet

user = UserViewSet.as_view({'get': 'retrieve'})
notes = NoteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
category = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('user/', user),
    path('notes/', notes),
    path('category/', category)
]
