# Generated by Django 3.2.21 on 2023-10-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='price',
            field=models.TextField(max_length=255),
            preserve_default=False,
        ),
    ]
