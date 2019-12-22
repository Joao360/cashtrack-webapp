# Generated by Django 2.1.7 on 2019-12-22 15:50

from django.db import migrations

def createCategories(apps, schema_editor):
    Category = apps.get_model('records', 'Category')
    Category.objects.create(name='Food')
    Category.objects.create(name='Transportation')

class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(createCategories),
    ]