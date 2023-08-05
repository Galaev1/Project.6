# Generated by Django 4.2.3 on 2023-07-22 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0012_alter_mailinglogs_server_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата следующей рассылки, (дд.мм.гггг)'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время начала рассылки, (чч:мм:сс)'),
        ),
    ]
