from rest_framework import serializers

from sitio.models import Noticia


class NoticiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'texto', 'fecha', 'archivada']


