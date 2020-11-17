from django.urls import path

from core.views.category import CategoryViewSet
from core.views.note import NoteViewSet
from core.views.user import UserViewSet

note_list = NoteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
note_detail = NoteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('user/me/', UserViewSet.as_view({'get': 'retrieve'})),
    path('user/register/', UserViewSet.as_view({'post': 'create'})),

    path('notes/', note_list),
    path('notes/<int:pk>/', note_detail),

    path('category/', category_list)
]
