from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from user.models import User
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from order.serializers import UserSerializer


@csrf_exempt
def user(request):
    if request.method == 'GET':
        user = User.objects.all()
        return render(request, 'user/user_list.html', {'user_list': user})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')

    elif request.method == 'POST':
        user_name = request.POST['user_name']
        try:
            user_info = User.objects.get(user_name=user_name)
            request.session['user_type'] = user_info.user_type
            return render(request, 'user/login_result.html', {'isSuccessed': True, 'user_info': user_info})
        except:
            pass
        return render(request, 'user/login_result.html', {'isSuccessed': False})
