# Generated by Django 3.2.6 on 2021-08-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_foreign_id_uniq'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='thumbnail',
            field=models.URLField(blank=True, help_text='The thumbnail for the media.', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='thumbnail',
            field=models.URLField(blank=True, help_text='The thumbnail for the media.', max_length=1000, null=True),
        ),
    ]
