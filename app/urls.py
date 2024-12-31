from app.views import home
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
