from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


# --------------MODELOS-------------------
from Datos.models import DatosModel

# -----------SERIALIZERS-------------------
from Datos.serializers import DatosModelSerializers

# -------------------VIEWS-----------------
class DatosModelView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer =  DatosModelSerializers(data = request.data, context = {'request': request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response("Error formato")
    
    def get(self, request, format=None):
        alumno = DatosModel.objects.all()
        serializer = DatosModelSerializers(alumno, many= True)
        return Response(serializer.data)

    def delete(self, request, id):
        alumno = DatosModel.objects.get(id=id)
        if(alumno.delete()):
            return Response("Removido")
        return Response("Error formato")

    def put(self, resquest, id):
        alumno = DatosModel.objects.get(id=id)
        serializer = DatosModelSerializers(alumno, data=resquest.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response("Editado")
        return Response("Error formato")