# Generated by Django 4.2.3 on 2023-07-21 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0006_alter_mailing_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='time',
            field=models.TimeField(default=datetime.time(19, 35, 20, 624768), verbose_name='Время начала рассылки (чч:мм:сс)'),
        ),
    ]
