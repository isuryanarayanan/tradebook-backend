import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

class TokenEngine():

    secret = None
    algorithm = None

    def getUserSecret(self):
        pass


class TokenGenerateView(APIView):
    """
    Generate token
    """
    permission_classes = ()

    response = None
    response_code = None

    def get(self, request):
        """Call token engine here"""
        
        self.response = "Token validated"
        self.response_code = 200
        return Response(self.response, self.response_code)
