from django.db import models
from django.contrib.auth.models import User
 
class Tarefa(models.Model):
    CATEGORY_NAME = (
        ('I', 'Inicializado'),
        ('E', 'Em Andamento'),
        ('F', 'Finalizado'),
    )
 
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField(null=True, blank=True)
    # data de vencimento da tarefa
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    category = models.CharField(max_length=1, choices=CATEGORY_NAME, default='I', null=False, blank=False)
 
    def _str_(self):
        return self.title
 
class Tag(models.Model):
    tag_name = models.CharField(max_length=70)
    tasks = models.ManyToManyField(Tarefa, related_name='tags')
 
    def _str_(self):
        return self.tag_name
   
class Comment(models.Model):
    comment_text = models.TextField(blank=True, null=True)
    fk_task = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='comments')
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
 
    def _str_(self):
        return self.comment_text
    
class Notificacao(models.Model):
    titulo = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    pessoa_notif = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Notificacao')
    descricao = models.TextField(blank=True, null=True)
 
    def _str_(self):
        return self.titulo

class Anexo(models.Model):
    aquivo = models.FileField(upload_to='uploads/')
    data = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Anexo')