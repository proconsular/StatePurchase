from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.map),
    url(r'^state/([a-z]+)$', views.state),
    url(r'^restart$', views.restart),
    url(r'^turn$', views.turn),
    url(r'^data/buildings/(\d+)$', views.getBuildingData),
    url(r'^data/companies/(\d+)$', views.getCompanyData),
    url(r'^fix/buildings/(\d+)$', views.fixBuilding),
    url(r'^modify/states/(\d+)/build/([a-z]+)$', views.buyBuilding),
    url(r'^modify/states/(\d+)/improve/([a-z]+)$', views.improveTech),
    url(r'^modify/states/(\d+)/clean/([a-z]+)$', views.clean),
    url(r'^states/(\d+)/attack/(\d+)/([a-z]+)$', views.attack)
]
