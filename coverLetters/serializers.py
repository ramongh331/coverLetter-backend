from .models import CoverLetter
from rest_framework import serializers

class CoverLetterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model it will serialize
        model = CoverLetter
        # fields to be includes
        fields = ['id', 'name', 'position', 'date', 'company', 'yoe', 'skill', 'expertise', 'passion', 'products']