# Generated by Django 4.1.7 on 2023-04-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('start_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('end_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('end_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]