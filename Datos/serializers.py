from rest_framework import serializers

from Datos.models import DatosModel

class  DatosModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = DatosModel
        fields = ('__all__')