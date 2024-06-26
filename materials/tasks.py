import smtplib
from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from materials.models import Course


@shared_task
def mailing_update_course(course_id):
    """Отправка письма об обновлении курса"""
    course = Course.objects.get(pk=course_id)
    subscription_list = course.subscription.all()
    user_list = [subscription.user for subscription in subscription_list]
    try:
        response = send_mail(subject='Обновление курса',
                             message=f'Курс "{course}" обновился!',
                             from_email=EMAIL_HOST_USER,
                             recipient_list=user_list,
                             fail_silently=False,
                             )
        return response
    except smtplib.SMTPException as ex:
        raise ex
