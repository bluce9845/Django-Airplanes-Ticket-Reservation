# Generated by Django 4.1 on 2024-12-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Airlanes', '0009_datapenumpang_rename_tgl_pergi_maskapai_tgl_takeoff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapenumpang',
            name='nik',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
