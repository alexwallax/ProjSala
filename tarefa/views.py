from django.http import JsonResponse
from rest_framework import viewsets, generics
from tarefa.models import Tarefa, Comment, Tag, Notificacao, Anexo
from tarefa.serializer import TarefaSerializers, ComentarioSerializers, TagSerializers, NotificacaoSerializers, AnexoSerializers, ListaComentarioSerializer, ListaTagSerializer

# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializers

class TarefaRetriveView(generics.RetrieveAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializers

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ComentarioSerializers

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializers

class AnexoViewSet(viewsets.ModelViewSet):
    queryset = Anexo.objects.all()
    serializer_class = AnexoSerializers

class ListaComentarioTarefa(generics.ListAPIView):
    ''''Listando os comentários por taks'''
    def get_queryset(self):
        queryset = Comment.objects.filter(fk_task=self.kwargs['pk'])
        return queryset 
    serializer_class = ListaComentarioSerializer


class ListaTagTarefa(generics.ListAPIView):
    ''''Listando as Tags por taks'''
    def get_queryset(self):
        queryset = Tag.objects.filter(fk_task=self.kwargs['pk'])
        return queryset 
    serializer_class = ListaTagSerializer