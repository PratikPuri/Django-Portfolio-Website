# Generated by Django 4.0.3 on 2022-04-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='skill',
            name='logo',
            field=models.ImageField(default='skill.png', null=True, upload_to=''),
        ),
    ]
