# Generated by Django 3.2.21 on 2023-10-28 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_slot_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='price',
            field=models.TextField(blank=True, null=True),
        ),
    ]