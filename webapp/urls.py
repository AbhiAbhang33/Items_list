from django.urls import path
from .views import item_list, item_create, item_update, item_delete

urlpatterns = [
    path('', item_list, name='item_list'),
    path('create/', item_create, name='item_create'),
    path('update/<int:pk>/', item_update, name='item_update'),
    path('delete/<int:pk>/', item_delete, name='item_delete'),
]
