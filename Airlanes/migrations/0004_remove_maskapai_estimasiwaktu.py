# Generated by Django 4.1 on 2024-12-10 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Airlanes', '0003_maskapai_estimasiwaktu_maskapai_jamberangkat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maskapai',
            name='estimasiWaktu',
        ),
    ]
