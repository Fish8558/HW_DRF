import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_strip_product(instance):
    product_name = f"{instance.paid_course if instance.paid_course else instance.paid_lesson}"
    stripe_product = stripe.Product.create(name=product_name)
    return stripe_product


def create_strip_price(product, payment):
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=payment.payment_amount * 100,
        product_data={"name": product.name},
    )
    return stripe_price


def create_strip_session(price):
    stripe_session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return stripe_session.get('id'), stripe_session.get('url')
