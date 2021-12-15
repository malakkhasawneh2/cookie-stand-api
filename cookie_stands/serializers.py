from rest_framework import serializers
from .models import Cookie_stands


class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie_stands
        fields = "__all__"
