# Generated by Django 4.1.5 on 2023-02-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0007_register_data_study'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_data',
            name='status',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
