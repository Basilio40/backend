from rest_framework import serializers
from core.models import ListaCompras



class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListaCompras
        fields = ['nome','proprietario']
        

