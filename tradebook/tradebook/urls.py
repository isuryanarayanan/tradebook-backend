from django.contrib import admin
from django.urls import path, include

VERSION = 'v1'

urlpatterns = [
    path(VERSION + '/admin/', admin.site.urls),
    path(VERSION + '/users/', include('users.urls'))
]
