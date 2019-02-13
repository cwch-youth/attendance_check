from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.attendance_list, name='attendance_list'),
]
