from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from materials.models import Course, Lesson
from materials.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='url')]


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()
