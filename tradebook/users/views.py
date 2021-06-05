""" API endpoint views """

# Module imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ValidateToken(APIView):
    """ API for validating token """

    # API setup
    permission_classes = (IsAuthenticated,)

    # Response variables
    response = "Validated"
    response_code = 200

    def get(self, request):
        return Response(self.response, self.response_code)

  
