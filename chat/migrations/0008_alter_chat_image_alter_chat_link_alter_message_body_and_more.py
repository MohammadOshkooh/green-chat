# Generated by Django 4.1 on 2022-08-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_message_contain_image_message_image_alter_chat_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='image',
            field=models.ImageField(blank=True, default='../static/img/index.png', null=True, upload_to='profile/group/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='link',
            field=models.CharField(default='0eJ3rCpqmF7ubzmA45qI', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(blank=True, default='body', null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, default='../static/img/index.png', null=True, upload_to='chat/image/%y/%m/%d/'),
        ),
    ]