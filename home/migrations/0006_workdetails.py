# Generated by Django 5.0.6 on 2024-07-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_aboutmemodel_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_project', models.PositiveIntegerField(blank=True, null=True)),
                ('happy_client', models.PositiveIntegerField(blank=True, null=True)),
                ('number_of_coffee', models.PositiveIntegerField(blank=True, null=True)),
                ('experience_years', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
