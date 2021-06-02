from django.db import models
from users.models import User

class Wallet(models.Model):
    """ Wallet to manage user funds """   

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)

    def addFunds(self, amount):
        """ Add funds to balance """
        self.balance = self.balance + amount

    def withdrawFunds(self, amount):
        """ Withdraw funds from balance """
        if self.balance >= amount:
            self.balance = self.balance - amount

    def resetFunds(self):
        """ Reset balance """
        self.balance = 0.0
