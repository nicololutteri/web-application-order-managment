"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from app.Connector import getToken

import json

from app.utilities import getRole, getUser, Role

def login(request):
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        try:
            token = getToken(username, password)
        
            response = HttpResponseRedirect('/orders')
            response.set_cookie('token', token)

            return response
        except:
            (auth, userinfo) = userStatus(request)

            return render(request,
                'app/login.html',
                {
                    'title': 'Login',
                    'year': datetime.now().year,

                    'auth': auth,
                    'userinfo': userinfo,
                })
    else:
        (auth, userinfo) = userStatus(request)

        return render(request,
            'app/login.html',
            {
                'title': 'Login',
                'year': datetime.now().year,

                'auth': auth,
                'userinfo': userinfo,
            })

def logout(request):
    assert isinstance(request, HttpRequest)

    response = HttpResponseRedirect('/')
    response.delete_cookie('token')
    return response
    
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    (auth, userinfo) = userStatus(request)

    return render(request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,

            'auth': auth,
            'userinfo': userinfo,
        })

def orders(request):
    assert isinstance(request, HttpRequest)
    
    token = request.COOKIES.get('token', None)
    if (token == None):
        return login(request)
    else:
        try:
            (user, role) = getUser(request)
        except:
            return HttpResponse('Unauthorized', status=401)

        (auth, userinfo) = userStatus(request)

        return render(request,
            'app/orders.html',
            {
                'title': 'Orders',
                'year': datetime.now().year,
                'role': role,
                
                'auth': auth,
                'userinfo': userinfo,
            })

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    (auth, userinfo) = userStatus(request)

    response = render(request,
        'app/about.html',
        {
            'title':'About',
            'message': 'Web application for the university course "Dynamic applications for the web"',
            'submessage': 'Nicolò Lutteri', 
            'year':datetime.now().year,

            'auth': auth,
            'userinfo': userinfo,
        })

    response.set_cookie(key='Test', value=10)
    return response

def logininfo(request):
    assert isinstance(request, HttpRequest)

    (auth, userinfo) = userStatus(request)

    response = render(request,
        'app/loginInfo.html',
        {
            'title': 'About',

            'role': userinfo,
            
            'auth': auth,
            'userinfo': userinfo,
        })

    return response

def userStatus(request):
    token = request.COOKIES.get('token', None)
    try:
        (user, role) = getUser(request)
    except:
        return (False, '')

    return (True, 'Username: ' + user + ", " + str(role))
