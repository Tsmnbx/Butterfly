from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^(?P<Scientific_Name>[0-9]+)/$',views.species_id, name='species_id')
]
