"""
Definition of views.
"""

from datetime import datetime, timedelta
from django.http import HttpRequest, HttpResponse
from rest_framework import request
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from django.http import JsonResponse

from django.contrib.auth import authenticate, login

from rest_framework.authtoken.models import Token

import jwt

JWT_EXP_DELTA_SECONDS = 99999

@api_view(['POST'])
def login(request, username):
    user = authenticate(request, username=username, password=request.POST.get('password', ''))

    if user == None:
        return HttpResponse('Unauthorized', status=401)
    elif user.groups.filter(name='Customer') or user.groups.filter(name='Manager') or user.groups.filter(name='Agent'):
        payload = {
            'user_id': username,
            'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }

        jwt_token = jwt.encode(payload, 'secret', 'HS256')
      
        return JsonResponse({'token': jwt_token})
    else:
        return HttpResponse('Unauthorized', status=401)

@api_view(['GET'])
def Home(request):
    data = {
        'status': 'Ready'    
    }

    return JsonResponse(data)
