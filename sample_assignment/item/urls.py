from django.urls import path

from .views import ItemViewSet

urlpatterns = [
    path('list',ItemViewSet.as_view({'get':'get'}),name='list'),
    path('retrive',ItemViewSet.as_view({'get':'retrive'}),name='retrive'),
    path('create',ItemViewSet.as_view({'post':'post'}),name='create'),
    path('update',ItemViewSet.as_view({'put':'put'}),name='update'),
    path('delete',ItemViewSet.as_view({'delete':'delete'}),name='delete'),
]