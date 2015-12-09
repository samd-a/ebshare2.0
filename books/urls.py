from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.renderbookshelf, name='bookshelf'),
    url(r'^upload/$', views.contribute_book, name='contribute_book'),
]