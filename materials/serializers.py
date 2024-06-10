from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()
