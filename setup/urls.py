
from django.contrib import admin
from django.urls import path, include
from tarefa.views import TarefaViewSet, TarefaRetriveView, ComentarioViewSet, TagViewSet, NotificacaoViewSet, AnexoViewSet, ListaComentarioTarefa
from rest_framework import routers 


router = routers.DefaultRouter()
router.register('tarefa', TarefaViewSet, basename='tarefa')
router.register('Comentario', ComentarioViewSet, basename='Commentario')
router.register('Tag', TagViewSet, basename='Tag')
router.register('Notificacao', NotificacaoViewSet, basename='Notificacao')
router.register('Anexo', AnexoViewSet, basename='Anexo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('Tarefa/<int:pk>/', TarefaRetriveView.as_view(), name="tarefa-retrive"),
    path('task/<int:pk>/comentarios/', ListaComentarioTarefa.as_view()),
]

