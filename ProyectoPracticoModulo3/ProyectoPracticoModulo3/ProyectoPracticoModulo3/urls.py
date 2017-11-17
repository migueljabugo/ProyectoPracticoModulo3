"""
Definition of urls for ProyectoPracticoModulo3.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^game\/(?P<id>[0-9]+)$', app.views.show_game),
    url(r'^new\/{0,1}$', app.views.new_game),
    url(r'^edit\/(?P<id>[0-9]+)\/{0,1}$', app.views.edit_game),
    url(r'^remove\/(?P<id>[0-9]+)\/{0,1}$', app.views.remove_game),
    url(r'^ranking\/{0,1}$', app.views.ranking),
    url(r'^search\/{0,1}$', app.views.search),
    url(r'', app.views.notFound),
]
