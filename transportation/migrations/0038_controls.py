# Generated by Django 5.0.4 on 2024-10-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0037_alter_rented_cars_renter_validid'),
    ]

    operations = [
        migrations.CreateModel(
            name='controls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control', models.IntegerField()),
            ],
        ),
    ]
