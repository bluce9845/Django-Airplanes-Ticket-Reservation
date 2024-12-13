# Generated by Django 4.1 on 2024-12-12 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Airlanes', '0010_alter_datapenumpang_nik'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10)),
                ('is_booked', models.BooleanField(default=False)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='Airlanes.maskapai')),
            ],
        ),
    ]
