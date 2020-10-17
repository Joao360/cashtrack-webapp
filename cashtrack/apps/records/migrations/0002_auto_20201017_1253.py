# Generated by Django 2.1.7 on 2020-10-17 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moneydeposit',
            name='ammount',
        ),
        migrations.RemoveField(
            model_name='record',
            name='ammount',
        ),
        migrations.AddField(
            model_name='moneydeposit',
            name='initial_amount',
            field=models.FloatField(default=0, verbose_name='amount of cash present in the deposit when it was registered'),
        ),
        migrations.AddField(
            model_name='record',
            name='amount',
            field=models.FloatField(default=0, verbose_name='amount of cash'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moneydeposit',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money_deposits', to=settings.AUTH_USER_MODEL),
        ),
    ]
