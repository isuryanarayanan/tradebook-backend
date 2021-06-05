""" Models for the funds app """

# Module imports
from django.db import models
from django.utils import timezone
from users.models import User


def get_time():
    """ Returns current time """
    return timezone.now

def get_timedelta(days):
    """ Returns a time from current time to the number of days passed """
    return timezone.now() + timezone.timedelta(days=days)


class Wallet(models.Model):
    """ Wallet to manage user funds """

    # Owner of the wallet
    wallet_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Wallet identifiers
    wallet_name = models.CharField(max_length=250)
    wallet_description = models.TextField(default='')
    # Timestamps
    wallet_created_on = models.DateTimeField(default=get_time())
    wallet_expiry_on = models.DateTimeField(
        default=get_timedelta(365))
    # Wallet budget
    wallet_balance = models.FloatField(default=0.0)

    def add_funds(self, amount):
        """ Add funds to balance """
        self.wallet_balance = self.wallet_balance + amount

    def withdraw_funds(self, amount):
        """ Withdraw funds from balance """
        if self.wallet_balance >= amount:
            self.wallet_balance = self.wallet_balance - amount

    def reset_funds(self):
        """ Reset balance """
        self.wallet_balance = 0.0


transaction_modes = (
    (1, 'deposit'),
    (2, 'withdraw')
)


class Transaction(models.Model):
    """ Transaction records each deposit and withdraw from the wallet """

    # Transaction belongs to
    tx_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    # Deposit or Withdrawal
    tx_mode = models.IntegerField(choices=transaction_modes)
    tx_amount = models.FloatField(default=0.0)
    tx_date = models.DateTimeField(default=get_time())
    # After transaction balance
    tx_resolved_balance = models.FloatField()
