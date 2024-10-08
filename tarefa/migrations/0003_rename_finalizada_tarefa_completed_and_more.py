# Generated by Django 5.1 on 2024-09-24 19:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0002_tarefa_usuario_alter_tarefa_data_finalizar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='finalizada',
            new_name='completed',
        ),
        migrations.RenameField(
            model_name='tarefa',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='tarefa',
            old_name='data_finalizar',
            new_name='due_date',
        ),
        migrations.RenameField(
            model_name='tarefa',
            old_name='data_inicio',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='tarefa',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='usuario',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='category',
            field=models.CharField(choices=[('I', 'Inicializado'), ('E', 'Em Andamento'), ('F', 'Finalizado')], default='I', max_length=1),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarefa',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fk_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tarefa.tarefa')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=70)),
                ('tasks', models.ManyToManyField(related_name='tags', to='tarefa.tarefa')),
            ],
        ),
    ]
