from rest_framework import serializers
from .models import PlayModels, Play
from .custom_error import PlainValidationError
from rest_framework import status


class PlaySerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayModels
        fields = '__all__'


class MainPlaySerializer(serializers.ModelSerializer):
    play = PlaySerializer(many=True, read_only=True)

    class Meta:
        model = Play
        fields = "__all__"

# class PlaySerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     date = serializers.DateField()

#     def create(self, validated_data):
#         return PlayModels.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

#     def validate(self, data):

#         if len(data.get('name')) <= 2:
#             raise serializers.ValidationError(
#                 {"name": "Name should be greater than 2 letters"}, code=422,)
