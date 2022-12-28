from django.urls import path
from crud import views

urlpatterns = [
    path('', views.index_view,name='index_view'),
    path('create', views.ClienteCreateView.as_view(), name='create_view'),
    path('read', views.ClienteListView.as_view(), name='read_view'),
    path('update/<pk>', views.ClienteUpdateView.as_view(), name='update_view'),
    path('delete/<pk>', views.ClienteDeleteView.as_view(), name='delete_view')
]
