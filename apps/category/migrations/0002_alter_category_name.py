# Generated by Django 4.2.6 on 2023-10-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
