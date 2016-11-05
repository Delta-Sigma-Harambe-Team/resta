from rest_framework import permissions, viewsets
from rest_framework.response import Response
from products.models import Resource
from products.serializers import ResourceSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.order_by('-created_at')  #Obligatorio
    serializer_class = ResourceSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS: return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def perform_create(self, serializer):
        instance = serializer.save()#author=self.request.user)
        return super(ResourceViewSet, self).perform_create(serializer)