from .models import Review
from rest_framework import serializers


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ['content', 'rating']

