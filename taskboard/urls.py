from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from .views import index, board_page, BoardViewSet, TasksViewSet

router = routers.DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'tasks', TasksViewSet)


urlpatterns = [
    path('', index, name='homepage'),
    path('<int:board_id>', board_page, name='boardpage'),
    path('api/', include(router.urls)),
]
