from rest_framework import serializers

from Profile.models import ProfileModel

class ProfileSerialiezers(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')