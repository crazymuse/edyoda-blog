from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login$',views.login,name='login'),
    url(r'^write$',views.write,name='write'),
    url(r'^profile$',views.profile,name='profile'),
    url(r'^userlogin$',views.userlogin,name='userlogin'),
    url(r'^userregister$',views.userregister,name='userregister')


]
