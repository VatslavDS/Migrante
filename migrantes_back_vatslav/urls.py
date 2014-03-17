from django.conf.urls import patterns, include, url
from main.views import buscarUsuario, registroMigrante, checkPoint, main

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^index/$', buscarUsuario),
    url(r'^registro/$', registroMigrante),
    url(r'^checkpoint/$', checkPoint),
    #Todavia no implemento main
    url(r'^main/', main),
    url(r'^admin/', include(admin.site.urls)),
    
)
