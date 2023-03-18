"""
Definition of views.
"""

from datetime import datetime
from django.http import HttpRequest, HttpResponse
from rest_framework import request
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from django.http import JsonResponse, HttpResponse
from django.core import serializers

from app.models import Agent, Customer, Order

from app.utilities import get_role, get_user, Role

@api_view(['GET'])
def Home(request):
    data = {
        'status': 'Ready'
    }

    return JsonResponse(data)

@api_view(['GET'])
def clientAllOrders(request):
    try:
        (user, role) = get_user(request)
    except:
        return HttpResponse('Unauthorized', status=401)

    if (role == Role.Customer):
        orders = Order.objects.filter(cust_code=user)
    elif (role == Role.Agent):
        orders = Order.objects.filter(agent_code=user)
    elif (role == Role.Manager):
        orders = Order.objects.all()
    else:
        return HttpResponse(status=500)

    serialized_queryset = serializers.serialize('json', orders)
    return JsonResponse(serialized_queryset, safe=False)

@api_view(['POST', 'PUT', 'DELETE'])
def getOrder(request, code = None):
    # In the demo modify and delete, is blocked
    return HttpResponse('Unauthorized', status=401)

    try:
        (user, role) = get_user(request)
    except:
        return HttpResponse('Unauthorized', status=401)

    if request.method == 'POST':
        orders = Order.objects.filter(ord_num = code)
        tmp = serializers.serialize('python', orders)

        if ((role == Role.Customer and tmp.cust_code == user) or (role == Role.Agent and tmp.agent_code == user) or role == Role.Manager):
            serialized_queryset = serializers.serialize('json', orders)
            return JsonResponse(serialized_queryset, safe=False)
        else:
            return HttpResponse('Unauthorized', status=401)
    elif request.method == 'PUT':
        ord_num = request.POST.get('ord_num', '')
        ord_amount = request.POST.get('ord_amount', '')
        advance_amount = request.POST.get('advance_amount', '')
        ord_date = request.POST.get('ord_date', '')
        cust_code = request.POST.get('cust_code', '')
        agent_code = request.POST.get('agent_code', '')
        ord_description = request.POST.get('ord_description', '')
     
        if ((user == agent_code and role == Role.Agent) or role == Role.Manager): 
            cust_code = Customer.objects.get(cust_code = cust_code)
            agent_code = Agent.objects.get(agent_code = agent_code)

            Order.objects.update_or_create(ord_num=ord_num,
                               defaults={
                                   'ord_num': ord_num,
                                   'ord_amount': ord_amount,
                                   'advance_amount': advance_amount,
                                   'ord_date': ord_date,
                                   'cust_code': cust_code,
                                   'agent_code': agent_code,
                                   'ord_description': ord_description,
                               })
   
            return JsonResponse({'status': 'done'})
        else:
            return HttpResponse('Unauthorized', status=401)
    elif request.method == 'DELETE':
        if (role == Role.Customer):
            return HttpResponse('Unauthorized', status=401)
        else:
            orders = Order.objects.get(ord_num = code)
            agent_code = orders.agent_code.agent_code

            if (agent_code == user or role == Role.Manager):
                Order.objects.filter(ord_num=code).delete()
                return JsonResponse({'status': 'done'})
            else:
                return HttpResponse('Unauthorized', status=401)

@api_view(['GET'])
def agentInfo(request, code):
    try:
        (user, role) = get_user(request)
    except:
        return HttpResponse('Unauthorized', status=401)

    # Controlo se ha avuto contatti con il cliente con l'agente
    orders = Order.objects.filter(agent_code = code, cust_code = user)

    if ((role == Role.Customer and orders.count() > 0) or role == Role.Manager):
        agents = Agent.objects.filter(agent_code=code)

        serialized_queryset = serializers.serialize('json', agents)
        return JsonResponse(serialized_queryset, safe=False)
    else:
        return HttpResponse('Unauthorized', status=401)

@api_view(['GET'])
def clientInfo(request, code):
    try:
        (user, role) = get_user(request)
    except:
        return HttpResponse('Unauthorized', status=401)

    # Controllo se ha avuto contatti con l'agente il cliente
    orders = Order.objects.filter(agent_code = user, cust_code = code)

    if ((role == Role.Agent and orders.count() > 0) or role == Role.Manager):
        clients = Customer.objects.filter(cust_code=code)

        serialized_queryset = serializers.serialize('json', clients)
        return JsonResponse(serialized_queryset, safe=False)
    else:
        return HttpResponse('Unauthorized', status=401)
