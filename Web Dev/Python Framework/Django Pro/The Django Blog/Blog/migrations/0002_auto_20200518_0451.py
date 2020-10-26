# Generated by Django 3.0.5 on 2020-05-17 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='tittle',
            new_name='title',
        ),
        migrations.AddField(
            model_name='blogs',
            name='slug',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
