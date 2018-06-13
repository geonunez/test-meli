from rest_framework import serializers

class MutantSerializer(serializers.Serializer):
    adn = serializers.ListField(required=True)
