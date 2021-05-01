from rest_framework import serializers


class AdministratorUserRegistrationSerializer(serializers.Serializer):
    """Serializer for making a user with administrator profile"""
    email = serializers.CharField(max_length=250)
    username = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=250, write_only=True)
    password1 = serializers.CharField(max_length=250, write_only=True)

    def validate(self, data):

        return data


class InvestorUserRegistrationSerializer(serializers.Serializer):
    """Serializer for making a user with investor profile"""
    email = serializers.CharField(max_length=250)
    username = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=250, write_only=True)
    password1 = serializers.CharField(max_length=250, write_only=True)
    first_name = serializers.CharField(max_length=250)
    last_name = serializers.CharField(max_length=250)
    initial_balance = serializers.IntegerField(default=0)

    def validate(self, data):
        return data
