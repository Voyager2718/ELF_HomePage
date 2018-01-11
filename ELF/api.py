from django.http import HttpResponse, JsonResponse, Http404

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def GetBugPost(request):
    if(request.is_ajax() and request.method == 'POST'):
        return HttpResponse(request.body)
    raise Http404('No data in request.')
