# Generated by Django 4.1 on 2024-12-10 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airlanes', '0005_alter_maskapai_hargaticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maskapai',
            name='hargaTicket',
            field=models.CharField(max_length=200),
        ),
    ]
