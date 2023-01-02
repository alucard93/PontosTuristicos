from rest_framework import serializers
from atracoes.models import Atracao

from atracoes.serializers import AtracaoSerializer
from enderecos.models import Endereco
from enderecos.serializers import EnderecoSerializer
from .models import PontoTuristico, DocIdentificacao

class DocIdentificacaoSerializer(serializers.Serializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(serializers.Serializer):
    atracoes = AtracaoSerializer(many=True)
    enderecoes = EnderecoSerializer()

    class Meta:
        model = PontoTuristico
        fields = [
            "id",
            "nome",
            "descrição",
            "aprovado",
            "atracoes",
            "comentarios",
            "avaliacoes",
            "endereco",
            "doc_identificacao"
        ]
        read_only_fields = ('comentarios', )

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.object.create(**atracao)
            ponto.atracoes.add(at)
            
    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        avaliacoes = validated_data['avaliacoes']
        del validated_data['avaliacoes']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        ponto.avaliacoes.set(avaliacoes)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto