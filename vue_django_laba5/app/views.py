from django.shortcuts import render
from django.views import View
import json

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