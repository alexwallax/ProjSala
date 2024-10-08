from tarefa.models import Tarefa, Comment, Tag, Notificacao, Anexo
from rest_framework import serializers

class TarefaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__' 
 

class ComentarioSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = '__all__'   

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class NotificacaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'

class AnexoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anexo
        fields = '__all__'