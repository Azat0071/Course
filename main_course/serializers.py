from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    duration = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def validate_title(self, value):
        if value.strip() == "":
            raise serializers.ValidationError("Пусто, повторите попытку")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Цена должна быть больше нуля')
        return value

    def validate_description(self, value):
        if value.strip() == "":
            raise serializers.ValidationError('Описание не может быть пустым')
        return value