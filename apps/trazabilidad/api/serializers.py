from rest_framework import serializers
from apps.trazabilidad.models import *

#p

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

class RealizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realiza
        fields = '__all__'

class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = '__all__'

class TipoCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCultivo
        fields = '__all__'

class SemilleroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semillero
        fields = '__all__'

class AsignacionActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionActividades
        fields = '__all__'

class ProgramacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programacion
        fields = '__all__'

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'

class CalendarioLunarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioLunar
        fields = '__all__'



#x

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'

class ErasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eras
        fields = '__all__'

class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = '__all__'

class PlantacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantacion
        fields = '__all__'

class PeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pea
        fields = '__all__'

class DesarrollanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desarrollan
        fields = '__all__'

class Tipo_residuosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_residuos
        fields = '__all__'

class ResiduosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residuos
        fields = '__all__'

class Control_fitosanitarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control_fitosanitario
        fields = '__all__'
