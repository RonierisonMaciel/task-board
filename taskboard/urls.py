from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from .views import index, board_page, BoardViewSet, TasksViewSet, new_task, new_board

router = routers.DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'tasks', TasksViewSet)


urlpatterns = [
    path('', index, name='homepage'),
    path('new-board', new_board, name='new-board'),
    path('<int:board_id>', board_page, name='boardpage'),
    path('<int:board_id>/new-task', new_task, name='new-task'),
    path('api/', include(router.urls)),
]
