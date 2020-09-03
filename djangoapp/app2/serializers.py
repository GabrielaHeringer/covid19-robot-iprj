
from django.conf import settings
from rest_framework import serializers

from app2.models import Novidade2


class NovidadeSerializer(serializers.ModelSerializer):
    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.
    data_publicacao = serializers.DateField(format=settings.DATE_FORMAT, required=False)
    dataPrimeiroAcesso = serializers.DateField(format=settings.DATE_FORMAT, required=False)
    class Meta:
        model = Novidade2
        # fields = '__all__'
        fields = ('resumo', 'titulo', 'idioma', 'autores', 'categoria', 'subject', 'dataPrimeiroAcesso', 'data_publicacao', 'portal', 'link_externo')
