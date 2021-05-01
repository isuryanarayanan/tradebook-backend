import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from users.serializers import (
    InvestorUserRegistrationSerializer, AdministratorUserRegistrationSerializer
)


class RegisterInvestorUserView(APIView):
    """
    API for creating an investor user
    """
    permission_classes = ()

    response = None
    response_code = None

    def respond(self, params):
        self.response = params[0]
        self.response_code = params[1]

    def post(self, request):
        serializer = InvestorUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            self.respond(params=[serializer.data, 200])
        else:
            self.respond(params=[serializer.errors, 400])

        return Response(self.response, self.response_code)


class RegisterAdministratorUserView(APIView):
    """
    API for creating an administrator user
    """
    permission_classes = ()

    response = None
    response_code = None

    def respond(self, params):
        self.response = params[0]
        self.response_code = params[1]

    def post(self, request):
        serializer =AdministratorUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            self.respond(params=[serializer.data, 200])
        else:
            self.respond(params=[serializer.errors, 400])

        return Response(self.response, self.response_code)


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
