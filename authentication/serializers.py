from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'created_at', 'updated_at',
                  'first_name', 'last_name','password',
                  'confirm_password',)# 'tagline', 
        read_only_fields = ('created_at', 'updated_at',)

    def create(self, validated_data):
        return Account.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        if self.validatePass(validated_data):
            instance.set_password(validated_data.get('password'))
            instance.save()
        update_session_auth_hash(self.context.get('request'), instance)
        return instance
    
    def validatePass(self,data):
        password = data.get('password', None)
        confirm_password = data.get('confirm_password', None)
        return password and confirm_password and password == confirm_password
