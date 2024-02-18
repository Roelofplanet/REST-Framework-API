from rest_framework import serializers
from .models import GovernmentData

class GovernmentDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GovernmentData
        fields = ('id', 'url', 'naam', 'inwoners', 'oppervlakte', 'hoofdplaats')