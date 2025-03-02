from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Endpoint for login
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Endpoint for token refresh
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]