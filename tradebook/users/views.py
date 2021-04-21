import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

class TokenValidationView(APIView):
    """
    API for validation a token
    """
    permission_classes = (IsAuthenticated,)

    response = None
    response_code = None

    def get(self, request):
        self.response = "Token validated"
        self.response_code = 200
        return Response(self.response, self.response_code)
