from django.urls import path
from funds.views import AddFundsView

urlpatterns = [
    path('add/', AddFundsView.as_view())
]
