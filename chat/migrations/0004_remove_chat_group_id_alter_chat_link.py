# Generated by Django 4.1 on 2022-08-28 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_chat_group_id_alter_chat_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='group_id',
        ),
        migrations.AlterField(
            model_name='chat',
            name='link',
            field=models.CharField(default='IQn9xh6JQ1qgfCl5Mj05', max_length=25, unique=True),
        ),
    ]
