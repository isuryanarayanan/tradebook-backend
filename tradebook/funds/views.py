""" API endpoint views """

# Module imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Application imports
from funds.serializers import (
    WalletSerializer,
    DepositFundsSerializer,
    WithdrawFundsSerializer,
    TransactionSerializer,
)
from users.models import User
from funds.models import Wallet


class WalletView(APIView):
    """ API for wallet operations """

    # API setup
    permission_classes = ()

    # Response variables
    response = None
    response_code = None

    def get(self, request):
        """ Get all wallets of request user """
        # obj_list = Wallet.objects.all().filter(wallet_user=request.user.id)
        obj_list = Wallet.objects.all().filter(wallet_user=1)
        self.response = {}
        for i in range(0, len(obj_list)):
            serializer = WalletSerializer(obj_list[i])
            if serializer.is_valid:
                self.response[obj_list[i].id] = serializer.data
                self.response_code = 200
            else:
                self.response = serializer.errors
                self.response_code = 400


        # API response using response variables
        return Response(self.response, self.response_code)

    def post(self, request):
        """ Method handling post request made to this API endpoint """

        serializer = WalletSerializer(data=request.data)

        if serializer.is_valid():
            request.data["wallet_user"] = User.objects.get(id=1)
            wallet = serializer.create(request.data)
            wallet.save()
            self.response = serializer.data
            self.response_code = 200
        else:
            self.response = serializer.errors
            self.response_code = 400

        # API response using response variables
        return Response(self.response, self.response_code)


class WalletDetailView(APIView):
    """ API for wallet detail operations """

    # API setup
    permission_classes = ()

    # Response variables
    response = None
    response_code = None

    def get(self, request, pk):
        """ Get all wallets of request user """
        try:
            # serializer = WalletSerializer(Wallet.objects.get(id=pk, wallet_user=request.user.id))
            serializer = WalletSerializer(
                Wallet.objects.get(id=pk, wallet_user=1))
            self.response = serializer.data
            self.response_code = 200
        except Wallet.DoesNotExist:
            self.response = "Wallet not found"
            self.response_code = 400

        # API response using response variables
        return Response(self.response, self.response_code)

    def put(self, request, pk):
        """ Method handling put request made to this API endpoint """

        instance = Wallet.objects.get(id=pk)
        request.data["wallet_user"] = User.objects.get(id=1)
        serializer = WalletSerializer(
            instance, data=request.data, partial=True)

        if serializer.is_valid():
            wallet = serializer.update(instance, request.data)
            wallet.save()
            self.response = serializer.data
            self.response_code = 200
        else:
            self.response = serializer.errors
            self.response_code = 400

        # API response using response variables
        return Response(self.response, self.response_code)

    def delete(self, request, pk):
        """ Method handling post request made to this API endpoint """
        try:
            # wallet = Wallet.objects.get(id=pk, wallet_user=request.user.id)
            wallet = Wallet.objects.get(id=pk, wallet_user=1)
            serializer = WalletSerializer(wallet)
            wallet.delete()
            self.response = serializer.data 
            self.response_code = 200
        except Wallet.DoesNotExist:
            self.response = "Wallet not found"
            self.response_code = 400

        # API response using response variables
        return Response(self.response, self.response_code)


class DepositFundsView(APIView):
    """ API for adding funds to the authenticated user """

    # API setup
    permission_classes = (IsAuthenticated,)

    # Response variables
    response = None
    response_code = None

    def post(self, request):
        """ Method handling post request made to this API endpoint """

        serializer = DepositFundsSerializer(data=request.data)
        if serializer.is_valid():
            self.response = serializer.data
            self.response_code = 200
        else:
            self.response = serializer.errors
            self.response_code = 400

        # API response using response variables
        return Response(self.response, self.response_code)


class WithdrawFundsView(APIView):
    """ API for withdrawing funds to the authenticated user """

    # API setup
    permission_classes = (IsAuthenticated,)

    # Response variables
    response = None
    response_code = None

    def post(self, request):
        """ Method handling post request made to this API endpoint """

        serializer = WithdrawFundsSerializer(data=request.data)
        if serializer.is_valid():
            self.response = serializer.data
            self.response_code = 200
        else:
            self.response = serializer.errors
            self.response_code = 400

        # API response using response variables
        return Response(self.response, self.response_code)
