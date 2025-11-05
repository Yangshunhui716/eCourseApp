from courses.models import Category, Course
from rest_framework import serializers

class CategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'created_date', 'image', 'category_id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['image'] = instance.image.url

        return data