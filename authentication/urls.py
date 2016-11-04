from django.conf.urls import url, include
from rest_framework_nested import routers
from authentication.views import *

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls,namespace = 'accounts')),
	url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
	url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
]


