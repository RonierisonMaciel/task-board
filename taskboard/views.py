from urllib.robotparser import RequestRate
from django.shortcuts import render, redirect
from .models import Board, Task
from rest_framework import viewsets
from .serializer import BoardSerializer, TaskSerializer
from .forms import TaskForm, BoardForm
from rest_framework.response import Response
from rest_framework.decorators import action


def index(request):

    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

        return redirect('homepage')


    context = {
        'boards': Board.objects.all()
    }
    return render(request, 'index.html', context)


def board_page(request, board_id: int):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

        redirect('boardpage', board_id=board_id)


    context = {
        'board_id': board_id,
        'tasks': Task.objects.all().filter(board_id=board_id),
        'status_list': Task.status_list
    }
    return render(request, 'board.html', context)


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False)
    def pending(self, request):
        queryset = Task.objects.all().filter(status='pending')
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=False)
    def doing(self, request):
        queryset = Task.objects.all().filter(status='doing')
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=False)
    def done(self, request):
        queryset = Task.objects.all().filter(status='done')
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=False)
    def help(self, request):
        queryset = Task.objects.all().filter(status='help')
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
