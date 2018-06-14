# -*- coding: utf-8 -*-

from rest_framework import serializers

class MutantSerializer(serializers.Serializer):
    adn = serializers.ListField(required=True)

    def validate_adn(self, value):
        hight = len(value)
        weigth = len(value[0])

        if hight != weigth:
            raise serializers.ValidationError('La matriz tiene que ser de NxN')

        if hight < 4:
            raise serializers.ValidationError('La matriz tiene que ser de al menos N=4')

        for i in range(1, len(value)):
            if weigth != len(value[i]):
                raise serializers.ValidationError('La matriz tiene que ser NxN')

        return value
