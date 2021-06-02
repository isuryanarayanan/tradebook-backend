""" Serializers for API views """

# Module imports
from rest_framework import serializers
from django.contrib.auth import authenticate

class AddFundsSerializer(serializers.Serializer):
    """ Serializer for 'funds/add/' endpoint """

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
