# Generated by Django 5.0.6 on 2024-07-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_aboutmemodel_contactmodel_projectmodel_servicesmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='aboutme_images/'),
        ),
    ]