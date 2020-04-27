from rest_framework import serializers
from .models import Spot

class SpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spot
        fields = ('id','url','name','geolocation','windDirection','rating')