# Generated by Django 4.0.3 on 2022-04-15 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_project_deploylink_alter_project_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deployLink',
            field=models.URLField(default='#'),
        ),
        migrations.AlterField(
            model_name='project',
            name='github',
            field=models.URLField(default='#'),
        ),
    ]