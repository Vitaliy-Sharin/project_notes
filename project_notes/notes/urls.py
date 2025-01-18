from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<int:id_user>/view_folder/<int:id_folder>', views.view_folder, name='view_folder'),
]