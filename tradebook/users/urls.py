from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from users.views import (
    TokenValidationView, RegisterInvestorUserView, RegisterAdministratorUserView
)
urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/validate/', TokenValidationView.as_view(), name='token_validate'),

    path('register/investor/', RegisterInvestorUserView.as_view(),
         name='users_register_investor'),
    path('register/administrator/', RegisterAdministratorUserView.as_view(),
         name='users_register_administrator'),
]
