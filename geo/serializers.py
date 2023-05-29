from rest_framework import serializers
from geo.get_tele_bot import bot_notification

from geo.models import Place
from user.serializers import UserSerializer


class PlaceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Place
        fields = ["id", "name", "description", "geom", "aproved", "user"]
        read_only_fields = ["aproved"]

    def create(self, validated_data):
        name = validated_data.get("name")
        desc = validated_data.get("description")
        geom = validated_data.get("geom")
        bot_notification(name, geom, desc)

        place = Place(**validated_data)

        place.save()
        return place


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "name", "description", "geom", "aproved", "user"]
        read_only_fields = ["aproved", "user"]


class PlaceDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Place
        fields = ["id", "name", "description", "geom", "aproved", "user"]
        read_only_fields = ["aproved", "user"]
