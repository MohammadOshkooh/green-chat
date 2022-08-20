# Generated by Django 4.1 on 2022-08-19 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0005_alter_chat_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='link',
            field=models.CharField(default='n2tZoxkFg9KgO8EMLvyb', max_length=50, unique=True),
        ),
        migrations.RemoveField(
            model_name='contactlist',
            name='contact',
        ),
        migrations.AddField(
            model_name='contactlist',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_list', to=settings.AUTH_USER_MODEL),
        ),
    ]