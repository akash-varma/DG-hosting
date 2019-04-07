
from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'firstApp'
urlpatterns = [
	url(r'^$', views.jewellery, name="jewellery"),
	url(r'^register/',views.register,name="register_user")
]
