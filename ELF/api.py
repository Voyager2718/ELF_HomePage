from django.http import HttpResponse, JsonResponse, Http404, HttpResponseForbidden

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.views.decorators.csrf import csrf_exempt

import json
import re

from status_code import *


@csrf_exempt
def GetBugPost(request):
    if(request.is_ajax() and request.method == 'POST'):
        return HttpResponse(request.body)
    raise Http404('No data in request.')


@csrf_exempt
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
                    username=body['username'], password=body['password'])
                user.save()
                return JsonResponse(getStatusJson(200))
        except:
            return HttpResponseForbidden()
    return HttpResponseForbidden('Request without proper data.')
