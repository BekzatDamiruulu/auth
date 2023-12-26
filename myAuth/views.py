from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PersonGet
from django.contrib.auth.hashers import check_password
from .models import RegistrationUser
from .serializers import RegistrationUserSerializer
from django.contrib.auth.hashers import make_password
class GetUser(APIView):
    def get(self, request, mail, password):
        try:
            user = RegistrationUser.objects.get(mail=mail)
            serializer = PersonGet(user)
            if check_password(password, user.password):
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Неверный пароль'}, status=status.HTTP_401_UNAUTHORIZED)
        except RegistrationUser.DoesNotExist:
            return Response({'message': 'Пользователь с такой почтой не найден'}, status=status.HTTP_404_NOT_FOUND)


class RegistrationUserView(APIView):
    def post(self, request):
        serializer = RegistrationUserSerializer(data=request.data)
        if serializer.is_valid():
            mail = serializer.validated_data['mail']
            password = serializer.validated_data['password']
            confirmPassword = serializer.validated_data['confirmPassword']
            if RegistrationUser.objects.filter(mail=mail).exists():
                return Response({'message': 'Пользователь с таким email уже существует'},status=status.HTTP_400_BAD_REQUEST)
            if password != confirmPassword:
                return Response({'message': 'Пароли не совпадают'}, status=status.HTTP_400_BAD_REQUEST)
            new_user = RegistrationUser(mail=mail, password=make_password(password),
                                        confirmPassword=make_password(confirmPassword))
            new_user.save()
            return Response({'message': 'Пользователь успешно зарегистрирован'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserView(APIView):
    def delete(self, request, mail):
        try:
            user = RegistrationUser.objects.get(mail=mail)
            user.delete()
            return Response({'message': 'Пользователь успешно удален'}, status=status.HTTP_200_OK)
        except RegistrationUser.DoesNotExist:
            return Response({'message': 'Пользователь с такой почтой не найден'}, status=status.HTTP_404_NOT_FOUND)
