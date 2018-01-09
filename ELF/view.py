from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os

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
    context = {}
    return render(request, "Pages/home/home.html", updateDictionary(generalContext, context))


def bbs(request):
    context = {}
    return render(request, "Pages/bbs/bbs.html", updateDictionary(generalContext, context))


def downloads(request):
    context = {}
    return render(request, "Pages/downloads/downloads.html", updateDictionary(generalContext, context))


def report_bug(request):
    context = {}
    return render(request, "Pages/report_bug/report_bug.html", updateDictionary(generalContext, context))


'''
API
'''


def redirect(request, target):
    context = {}
    return HttpResponse("Hyperlink invalid.", updateDictionary(generalContext, context))


def api(request, api):
    context = {}
    return HttpResponse("API not supported.", updateDictionary(generalContext, context))


def activate(request, activationCode, deviceCode):
    context = {}
    return HttpResponse("Invalid activation code.")
