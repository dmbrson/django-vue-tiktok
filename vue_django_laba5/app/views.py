from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
import logging

class FrontendTemplateView(View):

    def get(self, request):
        context = {
            'post_data': json.dumps({}),  # Пустой объект для GET-запроса
            'get_data': json.dumps(dict(request.GET))  # Сериализуем GET параметры
        }
        return render(request, 'index.html', context)

    def post(self, request):
        context = {
            'post_data': request.body.decode('utf-8'),  # Тело POST-запроса
            'get_data': json.dumps(dict(request.GET))  # Сериализуем GET параметры
        }
        return render(request, 'index.html', context)

logger = logging.getLogger(__name__)

class RegisterView(View):

    def post(self, request):
        logger.debug("Received request: %s", request.body)
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
            email = data.get('email', '')

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)

            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return JsonResponse({'message': 'User registered successfully'}, status=201)
        except Exception as e:
            logger.error("Error during registration: %s", str(e))
            return JsonResponse({'error': str(e)}, status=400)