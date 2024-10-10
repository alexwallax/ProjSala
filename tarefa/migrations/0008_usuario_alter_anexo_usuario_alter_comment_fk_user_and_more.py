# Generated by Django 5.1 on 2024-10-10 18:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0007_customuser_alter_anexo_usuario_alter_comment_fk_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=100)),
                ('data_nasc', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='anexo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Anexo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='fk_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notificacao',
            name='pessoa_notif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notificacao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
