from django.urls import path
from authenticator.views import TokenGenerateView

urlpatterns = [
    path('token/', TokenGenerateView.as_view()),
]
