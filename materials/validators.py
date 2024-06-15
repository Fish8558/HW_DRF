import re
from rest_framework import serializers


class UrlValidator:
    """Класс валидации поля url в уроке"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('youtube\.com')
        field_value = value.get(self.field)
        if not reg.search(field_value):
            raise serializers.ValidationError("Запрещенная ссылка! Разрешены только с доменом youtube.com")
