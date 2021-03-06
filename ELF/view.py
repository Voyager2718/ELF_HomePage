from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

# csrf
from django.views.decorators.csrf import csrf_exempt

import os

from ELF_Model.models import *
import ELF.api as api

generalContext = {
    "productName": "ELF",
    "baseDir": os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
}

'''
Useful functions
'''


def updateDictionary(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result


'''
Pages
'''


def hello(request):
    return HttpResponse("Hello, world!<br />This site is working properly! Back to <a href='/'>Home</a>.")


def home(request):
    context = {"pageTitle": "Home"}
    return render(request, "Pages/home/home.html", updateDictionary(generalContext, context))


def bbs(request):
    context = {"pageTitle": "BBS"}
    return render(request, "Pages/bbs/bbs.html", updateDictionary(generalContext, context))


def downloads(request):
    context = {"pageTitle": "Downloads"}
    return render(request, "Pages/downloads/downloads.html", updateDictionary(generalContext, context))


def report_bug(request):
    context = {"pageTitle": "Report a bug"}
    return render(request, "Pages/report_bug/report_bug.html", updateDictionary(generalContext, context))


'''
API
'''


def redirect(request, target):
    context = {}
    raise Http404('Redirection nout found.')


@csrf_exempt
def api_distribute(request, api_name):
    try:
        return {
            'GetBugPost': api.GetBugPost,
            'CreateUser': api.CreateUser,
            'Login': api.Login,
            'Logout': api.Logout,
        }[api_name](request)
    except KeyError:
        raise Http404("API not found.")


def activate(request, activationCode, deviceCode):
    context = {}
    return HttpResponse(activationCode)
    return HttpResponse("Invalid activation code.")


'''
Test
'''


def test(request, user, password):
    return HttpResponse('Nothing to show.')
