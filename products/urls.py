from django.conf.urls import url, include
from rest_framework_nested import routers
from products.views import ResourceViewSet

router = routers.SimpleRouter()
router.register(r'products', ResourceViewSet)

urlpatterns = [
	url(r'^api/v1/', include(router.urls)),
]