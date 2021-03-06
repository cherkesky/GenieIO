"""GenieIO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token
from genieioapp.views import register_user, login_user
from genieioapp.views import Users, Wishes, Words, Wishers, Categories, Locations, Grants, Wish_Words, Words_Counter

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', Users, 'user')
router.register(r'wishers', Wishers, 'wisher')
router.register(r'wishes', Wishes, 'wish')
router.register(r'grants', Grants, 'grant')
router.register(r'words', Words, 'word')
router.register(r'wish_words', Wish_Words, 'wish_word')
router.register(r'categories', Categories, 'category')
router.register(r'locations', Locations, 'location')
router.register(r'words_counter', Words_Counter, 'word_counter')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register/', register_user),
    path('login/', login_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),]

urlpatterns += router.urls
