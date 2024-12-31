from django.urls import path
from client_app.views import home,create_staff,get_staff

urlpatterns = [
    path('', home, name='home'),
    path('create_staff/', create_staff, name='create_staff'),
    path('get_staff/', get_staff, name='get_staff'),
]