
'''from django.contrib import admin
from tarefa.models import Tarefa

# Register your models here.
class Tarefas(admin.ModelAdmin):
    list_display = ('id','name', 
                    'descricao', 
                    'data_inicio',
                    'data_finalizar',
                    'finalizada', 
                    'usuario')
    list_display_links = ('id', 'name')

admin.site.register(Tarefa, Tarefas)
'''

from django.contrib import admin
from tarefa.models import Tarefa, Tag, Comment
 
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'due_date', 'completed')
    list_filter = ['user', 'completed']
    list_display_links = ('id', 'title',)
    list_editable = ('completed',)
    search_fields = ('title',)
    list_per_page = 10
 
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name' )
    list_display_links = ('id', 'tag_name',)
    search_fields = ('tag_name',)
    list_per_page = 10
 
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_text', 'fk_task', 'created_at')
    list_display_links = ('id', 'comment_text',)
    search_fields = ('comment_text',)
    list_per_page = 10
 
admin.site.register(Tarefa, TasksAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)

