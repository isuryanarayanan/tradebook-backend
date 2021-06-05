""" Serializers for API views """

# Module imports
from rest_framework import serializers
from django.contrib.auth import authenticate
from funds.models import Wallet


class TransactionSerializer(serializers.Serializer):
    """ Serializer for transaction model """
    pass


class WalletSerializer(serializers.Serializer):
    """ Serializer for 'get-wallet' endpoint """

    # Incoming data from request
    wallet_name = serializers.CharField(max_length=250)
    wallet_description = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        """ Create a wallet object with the data received """
        return Wallet(**validated_data)

    def update(self, instance, validated_data):
        """ Update a wallet with new data """
        instance.wallet_name = validated_data.get(
            'wallet_name', instance.wallet_name)
        instance.wallet_description = validated_data.get(
            'wallet_description', instance.wallet_description)
        return instance


class DepositFundsSerializer(serializers.Serializer):
    """ Serializer for 'deposit-wallet' endpoint """

    # Incoming data from request
    amount = serializers.FloatField()

    # response data generated
    status = serializers.BooleanField(default=False, read_only=True)
    status_message = serializers.CharField(max_length=1000, read_only=True)

    def validate(self, data):
        """ Method to validate the data received and to generate and output """
        return {
            'status': data.get('user')
        }


class WithdrawFundsSerializer(serializers.Serializer):
    """ Serializer for 'withdraw-wallet' endpoint """

    # Incoming data from request
    amount = serializers.FloatField()

    # response data generated
    status = serializers.BooleanField(default=False, read_only=True)
    status_message = serializers.CharField(max_length=1000, read_only=True)

    def validate(self, data):
        """ Method to validate the data received and to generate and output """
        return {
            'status': data.get('user')
        }
