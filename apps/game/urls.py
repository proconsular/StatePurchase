from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.map),
    url(r'^state/([a-z]+)$', views.state),
    url(r'^restart$', views.restart),
    url(r'^turn$', views.turn)
]
