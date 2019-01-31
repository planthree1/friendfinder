from django.http import JsonResponse

def send_ok():
    return JsonResponse({"Result": "ok"})

def check_parameters(request, *args):
    for arg in args:
        if arg not in request.GET:
            raise Exception(arg + " parameter not found")