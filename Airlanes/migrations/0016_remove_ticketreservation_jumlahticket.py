# Generated by Django 4.1 on 2024-12-16 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Airlanes', '0015_maskapai_clas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketreservation',
            name='jumlahTicket',
        ),
    ]
