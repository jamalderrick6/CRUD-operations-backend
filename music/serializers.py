from rest_framework import serializers
from .models import Song


class SongListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
