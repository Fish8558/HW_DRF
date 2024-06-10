from django.contrib import admin
from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('email',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_date', 'payment_amount', 'payment_method',)
    list_filter = ('user', 'payment_method',)
    search_fields = ('paid_course', 'paid_lesson',)
