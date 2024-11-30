from rest_framework import serializers
from .models import ToDoTask

class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = '__all__'