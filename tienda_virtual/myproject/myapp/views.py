from rest_framework import viewsets
from myapp.models import *
from myapp.serializers import *

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class Usuario_view_login(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_serializer

class Usuario_view_registro(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_serializer

class TokenProvider(ObtainAuthToken):
    def post(self,  request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        user.token = token.key
        user.save()
        usuario = Usuario_serializer(user)
        return Response(usuario.data)
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.http import JsonResponse



# def registro(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = User.objects.create_user(username=username, password=password)
#         token, created = Token.objects.get_or_create(user=user)
#         return JsonResponse({'token': token.key})
#     return render(request, 'registro.html')


# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})
#     return Response({'error': 'Invalid Credentials'}, status=400)

# def redirect_view(request):
#     return redirect('/login/')

# @login_required
# def inicio(request):
#     return render(request, 'inicio.html')
