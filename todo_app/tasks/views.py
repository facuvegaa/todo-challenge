import jwt
from rest_framework import filters, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tasks.serializers import TaskSerializer

from .models import Task

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def CreateTask(request, format=None):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
    
    request.data['user'] = payload['id']
    task = request.data
    serializer = TaskSerializer(data=task, many=False)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def DeleteTask(request, pk):
    try:
        task = Task.objects.get(id=pk)
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated!')


        task = Task.objects.get(id=pk)

    
        if task.user.id != int(payload['id']):
                raise AuthenticationFailed('You can not delete a task that is not yours!')
        else:
                task.delete()
                return Response("Taks {} deleted succesfully".format(pk), status.HTTP_202_ACCEPTED)
    except:
        return Response("Taks {} does not exist".format(pk), status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def GetAllTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    if serializer.data == []:
        return Response("There are no games")
    return Response(serializer.data, status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def UpdateTask(request, pk):
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated!')

        task = Task.objects.get(id=pk)
        if task.user.id != int(payload['id']):
            raise AuthenticationFailed('You can not update a task that is not yours!')
        else:

            if not 'body' in request.data:
                request.data['body'] = task.body
            if not 'completed' in request.data:
                request.data['completed'] = task.completed
            serializer = TaskSerializer(instance=task, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
    except:
        return Response("Taks {} does not exist".format(pk), status.HTTP_400_BAD_REQUEST)

class FilterGet(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['body','created_at']
