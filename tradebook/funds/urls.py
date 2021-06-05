from django.urls import path
from funds.views import (
    DepositFundsView,
    WithdrawFundsView,
    WalletView,
    WalletDetailView
)

urlpatterns = [
    # Wallet operations
    path('wallet/deposit/',
         DepositFundsView.as_view(), name="deposit-wallet"),
    path('wallet/withdraw/',
         WithdrawFundsView.as_view(), name="withdraw-wallet"),

    path('wallet/', WalletView.as_view(), name="wallet"),
    path('wallet/<int:pk>/', WalletDetailView.as_view(), name="wallet-detail"),
    # Transaction operations

]
