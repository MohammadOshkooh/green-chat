# Generated by Django 4.0.6 on 2022-07-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_chat_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='link',
            field=models.CharField(default='wLkvez6YzMs6eTA62byE', max_length=50, unique=True),
        ),
    ]
