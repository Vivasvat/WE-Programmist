from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index_auth, name = 'index_auth'),
    path('index/', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('delete/<int:id>', views.delete, name = 'delete'),
]
