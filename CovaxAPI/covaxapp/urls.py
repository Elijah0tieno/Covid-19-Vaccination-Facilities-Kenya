from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^facilities$', views.facilitiesApi),
    url(r'^facilities/([0-9]*5)$', views.facilitiesApi),
    url(r'^counties$', views.countiesApi)
    # url(r'^counties/(?P<County>=\w{1,100})', views.countiesApi)
]
