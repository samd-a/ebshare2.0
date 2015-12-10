from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<book_id>[0-9]+)$', views.renderviewbook, name='viewbook'),
    url(r'^(?P<book_id>[0-9]+)/add_review/$',views.add_review,name="add_review"),
]