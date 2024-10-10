from django.http import JsonResponse
from rest_framework import viewsets, generics
from tarefa.models import Tarefa, Comment, Tag, Notificacao, Anexo
from tarefa.serializer import TarefaSerializers, ComentarioSerializers, TagSerializers, NotificacaoSerializers, AnexoSerializers, ListaComentarioSerializer, ListaTagSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializers
    authentication_classes = [BasicAuthentication]
    Permission_classes = [IsAuthenticated]

class TarefaRetriveView(generics.RetrieveAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializers
    authentication_classes = [BasicAuthentication]
    Permission_classes = [IsAuthenticated]

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ComentarioSerializers
    authentication_classes = [BasicAuthentication]
    Permission_classes = [IsAuthenticated]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    authentication_classes = [BasicAuthentication]
    Permission_classes = [IsAuthenticated]

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializers
    authentication_classes = [BasicAuthentication]
    Permission_classes = [IsAuthenticated]

class AnexoViewSet(viewsets.ModelViewSet):
    queryset = Anexo.objects.all()
    serializer_class = AnexoSerializers
    authentication_classes = [BasicAuthentication]
    Permission_classes = [IsAuthenticated]

class ListaComentarioTarefa(generics.ListAPIView):
    ''''Listando os comentários por taks'''
    def get_queryset(self):
        queryset = Comment.objects.filter(fk_task=self.kwargs['pk'])
        return queryset 
    serializer_class = ListaComentarioSerializer
    authentication_classes = [BasicAuthentication]
    Permission_classes = [IsAuthenticated]


class ListaTagTarefa(generics.ListAPIView):
    ''''Listando as Tags por taks'''
    def get_queryset(self):
        queryset = Tag.objects.filter(fk_task=self.kwargs['pk'])
        return queryset 
    serializer_class = ListaTagSerializer
    authentication_classes = [BasicAuthentication]
    Permission_classes = [IsAuthenticated]



