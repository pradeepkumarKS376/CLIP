# Generated by Django 4.0.8 on 2022-10-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0005_rename_ststus_general_models_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general_models',
            name='Client_contact',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
