from django.conf.urls import include
from django.urls import path
from trekcorderserverapi.views import register_user, login_user, ItemView
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'items', ItemView, 'item')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
