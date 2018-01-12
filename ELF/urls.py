from django.conf.urls import url
from . import view

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^home/$', view.home),
    url(r'^bbs/$', view.bbs),
    url(r'^downloads/$', view.downloads),
    url(r'^report_bug/$', view.report_bug),
    url(r'^individual_account/$', view.individual_account),

    url(r'^redirect/([a-zA-Z0-9\-\_\.]*)/$', view.redirect),
    url(r'^api/([a-zA-Z0-9\-\_\.]*)/$', view.api),
    url(r'^activate/([a-zA-Z0-9\-]*)/([a-zA-Z0-9\-]*)/$', view.activate),

    url(r'^$', view.home)
]
