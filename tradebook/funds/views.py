""" API endpoint views """

# Module imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from funds.serializers import AddFundsSerializer

class AddFundsView(APIView):
    """ API for adding funds to the authenticated user """

    # API setup
    permission_classes = (IsAuthenticated,)

    # Response variables
    response = None
    response_code = None

    def post(self, request):
        """ Method handling post request made to this API endpoint """

        serializer = AddFundsSerializer(data=request.data)
        if serializer.is_valid():
            self.response = serializer.data
            self.response_code = 200
        else:
            self.response = serializer.errors
            self.response_code = 400

        # API response using response variables
        return Response(self.response, self.response_code)

    
