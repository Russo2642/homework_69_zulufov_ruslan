from django.shortcuts import render
from django.http import JsonResponse
import json


def index_view(request):
    return render(request, 'index.html')


def add_view(request, *args, **kwargs):
    result = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            number_1 = float(data.get('number_1'))
            number_2 = float(data.get('number_2'))
            result = number_1 + number_2
            answer = {
                'result': result
            }
            return JsonResponse(answer, safe=False)
        except Exception as e:
            response = JsonResponse({'error': str(e)})
            response.status_code = 400
            return response
        

def sub_view(request, *args, **kwargs):
    result = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            number_1 = float(data.get('number_1'))
            number_2 = float(data.get('number_2'))
            result = number_1 - number_2
            answer = {
                'result': result
            }
            return JsonResponse(answer, safe=False)
        except Exception as e:
            response = JsonResponse({'error': str(e)})
            response.status_code = 400
            return response
        

def multi_view(request, *args, **kwargs):
    result = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            number_1 = float(data.get('number_1'))
            number_2 = float(data.get('number_2'))
            result = number_1 * number_2
            answer = {
                'result': result
            }
            return JsonResponse(answer, safe=False)
        except Exception as e:
            response = JsonResponse({'error': str(e)})
            response.status_code = 400
            return response
        

def divide_view(request, *args, **kwargs):
    result = 0
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            number_1 = float(data.get('number_1'))
            number_2 = float(data.get('number_2'))
            result = number_1 / number_2
            answer = {
                'result': result
            }
            return JsonResponse(answer, safe=False)
        except Exception as e:
            response = JsonResponse({'error': str(e)})
            response.status_code = 400
            return response
