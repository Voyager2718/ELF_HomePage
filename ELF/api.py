from django.http import HttpResponse, JsonResponse, Http404, HttpResponseForbidden

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views.decorators.csrf import csrf_exempt

from django.core.exceptions import PermissionDenied

import json
import re

from ELF.status_code import *


def CreateUser(request):
    if(request.is_ajax() and request.method == 'POST'):
        try:
            body = json.loads(request.body)
            try:
                if not bool(re.match('^[a-zA-Z][a-zA-Z0-9]{3,15}$', body['username'])):
                    return JsonResponse(getStatusJson(1001))
                if len(body['password']) > 32:
                    return JsonResponse(getStatusJson(1002))
                u = User.objects.get(username=body['username'])
                return JsonResponse(getStatusJson(1000))
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=body['username'], password=body['password'], email=body['email'])
                user.save()
                user = authenticate(
                    request, username=body['username'], password=body['password'])
                login(request, user)
                return JsonResponse(getStatusJson(200))
        except:
            return HttpResponseForbidden()
    return HttpResponseForbidden()


def Login(request):
    if(request.is_ajax() and request.method == 'POST'):
        try:
            body = json.loads(request.body)
            user = authenticate(
                request, username=body['username'], password=body['password'])
            if user is not None:
                login(request, user)
                return JsonResponse(getStatusJson(200))
            else:
                return JsonResponse(getStatusJson(1003))
        except PermissionDenied:
            return JsonResponse(getStatusJson(1004))
        except:
            return HttpResponseForbidden()
    return HttpResponseForbidden()


def Logout(request):
    try:
        logout(request)
        return JsonResponse(getStatusJson(200))
    except:
        return HttpResponseForbidden()


def GetBugPost(request):
    if(request.is_ajax() and request.method == 'POST'):
        return HttpResponse(request.body)
    return HttpResponseForbidden()
