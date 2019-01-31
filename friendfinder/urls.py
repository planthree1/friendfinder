"""friendfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from friend_finder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_user', views.get_all_user, name="get_user"),
    path('get_user_groups', views.get_group, name="get_user_goups"),
    path('add_user', views.add_user, name="add_user"),
    path('add_group', views.add_group, name="add_user"),
    path('add_group_user', views.add_group_user, name="add_user"),
    path('update_coordinates', views.update_coordinates, name="update_coordinates"),
    path('get_id', views.get_id, name="get_id"),
    path('get_user_from_group', views.get_user_from_group, name="get_user_from_group"),
    path('delete_group', views.delete_group, name="delete_group")
]
