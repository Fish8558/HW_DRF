from rest_framework import serializers
from materials.models import Course, Lesson, Subscription
from materials.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='url')]


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscribe(self, course):
        user = self.context['request'].user
        if Subscription.objects.filter(course=course, user=user):
            return f"Вы подписаны"
        return f"Вы не подписаны"
