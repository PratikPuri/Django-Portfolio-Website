# Generated by Django 4.0.3 on 2022-04-15 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_project_deploylink_alter_project_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deployLink',
            field=models.URLField(blank=True, default='#', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='github',
            field=models.URLField(blank=True, default='#', null=True),
        ),
    ]