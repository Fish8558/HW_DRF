from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.models import User, Payments
from users.permissions import IsOwnerOrReadOnly
from users.serializers import UserSerializer, UserDetailSerializer, PaymentsSerializer, UserRegisterSerializer, \
    UserNoOwnerSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from users.services import create_strip_product, create_strip_price, create_strip_session


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user == self.get_object():
            return UserDetailSerializer
        else:
            return UserNoOwnerSerializer


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ('payment_date',)
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product_id = create_strip_product(payment)
        price_id = create_strip_price(product_id, payment)
        payment.payment_id, payment.payment_link = create_strip_session(price_id)
        payment.save()
