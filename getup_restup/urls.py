"""getup_restup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from quickstart import views as qs_views
from snippets import views as sn_views

# router = routers.DefaultRouter()
# router.register(r'users', qs_views.UserViewSet)
# router.register(r'groups', qs_views.GroupViewSet)
# router.register(r'snippets', sn_views.SnippetList)

urlpatterns = [
    path('', qs_views.api_root),
    path('snippets/', include('snippets.urls')),
    path('users/', qs_views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', qs_views.UserDetail.as_view(), name='user-detail'),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
