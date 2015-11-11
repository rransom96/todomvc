from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import TodoSerializer
from todo.models import Todo


@api_view(['GET', 'POST'])
def list_create_todo(request):
    if request.method == "GET":
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailUpdateTodo(APIView):

    def get(self, request, pk, format=None):

        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)