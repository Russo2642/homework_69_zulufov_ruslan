from django.http import JsonResponse


def calculation_view(request, *args, **kwargs):
    result = 0
    try:
        data = {
            'A': 100,
            'B': 200
        }
        if request.path == '/add/':
            result = int(data['A'] + data['B'])
        elif request.path == '/subtract/':
            result = int(data['A'] - data['B'])
        elif request.path == '/multiply/':
            result = int(data['A'] * data['B'])
        elif request.path == '/divide/':
            result = float(data['A'] / data['B'])

        answer = {
            'answer': result
        }
        return JsonResponse(answer)
    except Exception as e:
        response = JsonResponse({'error': str(e)})
        response.status_code = 400
        return response
