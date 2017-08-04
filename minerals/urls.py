from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_minerals, name='list'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'first_letter/(?P<alpha>\w)', views.minerals_by_first_letter, name='minerals_by_first_letter'),
    url(r'group/(?P<group>\w+\s*)', views.minerals_by_group, name='minerals_by_group'),
    url(r'search/$', views.search, name='search'),
]