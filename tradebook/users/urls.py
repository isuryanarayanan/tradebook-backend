from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from users.views import ValidateToken

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/validate/', ValidateToken.as_view(), name='token_validate'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
