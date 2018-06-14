from rest_framework import serializers

class MutantSerializer(serializers.Serializer):
    adn = serializers.ListField(required=True)

    def validate_adn(self, value):
        hight = len(value)
        weigth = len(value[0])

        # Have to be NxN
        if hight != weigth:
            raise serializers.ValidationError('La matriz tiene que ser de NxN')

        for i in range(1, len(value)):
            if weigth != len(value[i]):
                raise serializers.ValidationError('La matriz tiene que ser NxN')

        return value
