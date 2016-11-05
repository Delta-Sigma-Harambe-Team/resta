from rest_framework import serializers
from authentication.serializers import *
from products.models import Resource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('id', 'name', 'amount','due_date')
        read_only_fields = ('id','created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(ResourceSerializer, self).get_validation_exclusions()
        return exclusions #+ ['author']

    def validate(self, data):
    	if data['due_date'] < data['created_at']:
            raise serializers.ValidationError("Due date can't be before today")
    	return data