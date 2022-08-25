import datetime

import jwt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


# Create your views here.
@api_view(['POST'])
def RegisterView(request, format=None):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)



@api_view(['POST'])
def LoginView(request, format=None):
    email = request.data['email']
    password = request.data['password']
    user = User.objects.filter(email=email).first()
    
    if user is None:
        raise AuthenticationFailed('User not found!')
    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect password!')
    
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
    response = Response()
    
    response.set_cookie(key='jwt', value=token, httponly=True)

    response.data = {
        'jwt': token
    }
    return response


@api_view(['POST'])
def LogoutView(request, format=None):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return Response(response.data, status.HTTP_200_OK)
