# Generated by Django 5.0.6 on 2024-07-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_aboutmemodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmemodel',
            name='my_intro',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
