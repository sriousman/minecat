from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='list'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
]