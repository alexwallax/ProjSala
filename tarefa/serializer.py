from tarefa.models import Tarefa, Comment, Tag, Notificacao, Anexo, Usuario
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

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class NotificacaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'

class AnexoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anexo
        fields = '__all__'

class ListaComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['fk_user', 'comment_text', 'fk_tarefa'] 
    
class ListaTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_name', 'fk_task'] 
	
class ListaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'email'] 