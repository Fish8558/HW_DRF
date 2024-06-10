from django.urls import path
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsListAPIView, PaymentsCreateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payment_list'),
    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payment_create'),
] + router.urls
