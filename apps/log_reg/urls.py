from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^state_purchase', views.prompt),
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^logout', views.logout),
    url(r'^create', views.create),
    url(r'^home$', views.home),
]
