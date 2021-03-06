# Generated by Django 2.1.7 on 2020-09-22 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name of the deposit')),
                ('ammount', models.FloatField(default=0, verbose_name='ammount of cash present in the deposit')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money_deposit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recordType', models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense')], default='Income', max_length=64)),
                ('ammount', models.FloatField(verbose_name='ammount of cash')),
                ('entity', models.CharField(blank=True, max_length=64, verbose_name='the other entity in the tradeoff')),
                ('datetime', models.DateTimeField()),
                ('note', models.CharField(blank=True, max_length=256)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Category')),
                ('money_deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='records.MoneyDeposit')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Category')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='moneydeposit',
            unique_together={('owner', 'name')},
        ),
    ]
