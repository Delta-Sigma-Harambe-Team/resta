from django.conf.urls import url, include
from rest_framework_nested import routers
from .views import *

urlpatterns = [
	url(r'^api/v1/products', Products.as_view()),
]