from rest_framework import serializers
from .models import Course, Student

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'