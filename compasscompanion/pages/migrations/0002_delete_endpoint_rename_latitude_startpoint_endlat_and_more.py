# Generated by Django 4.1.7 on 2023-04-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EndPoint',
        ),
        migrations.RenameField(
            model_name='startpoint',
            old_name='latitude',
            new_name='endlat',
        ),
        migrations.RenameField(
            model_name='startpoint',
            old_name='longitude',
            new_name='endlong',
        ),
        migrations.AddField(
            model_name='startpoint',
            name='startlat',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startpoint',
            name='startlong',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]