# Generated by Django 2.0.8 on 2019-01-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_remove_contentprovider_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentprovider',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
