# Generated by Django 4.0.3 on 2022-04-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deployLink',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.URLField(null=True),
        ),
    ]
