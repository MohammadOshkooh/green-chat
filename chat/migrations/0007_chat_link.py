# Generated by Django 4.0.6 on 2022-07-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_chat_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='link',
            field=models.CharField(default='KqcwznEPLXN78dJegBbR', max_length=50),
        ),
    ]