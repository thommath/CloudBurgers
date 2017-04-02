from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^setup/', views.setup, name='setup'),
]
