from django.conf.urls import patterns, include, url
from django.contrib import admin
from PiApp.views import *
from PiApp.api import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 

from common import globaldata
import os
import sys

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PiHome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', login_view),
    (r'^accounts/logout/$', logout_view),
    (r'^accounts/register/$', register_view),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns ('',
    (r'^$', include('PiApp.urls')),
    (r'^PiApp/', include('PiApp.urls')),
    (r'^filemanager/', include('filemanager.urls')),
    (r'^API/', include('PiHome.api_urls')),
)


app_urlpatterns = patterns('',)

cwd  = globaldata.APP_DIR
list = os.listdir(cwd)
sys.path.append(cwd);

for item in list:
    if os.path.isdir(os.path.join(cwd, item)):
        app_urlpatterns += patterns ('',
            (r'^App/' + item + '/', include(item + '.urls')),
            )

urlpatterns += app_urlpatterns

if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,
        }),
   )

handler404 = 'PiApp.views.fzf_view'
handler500 = 'PiApp.views.fzz_view'
