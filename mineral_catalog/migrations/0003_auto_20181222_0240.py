# Generated by Django 2.1.3 on 2018-12-22 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mineral_catalog', '0002_auto_20181222_0237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mineral',
            options={'ordering': ['slug']},
        ),
    ]
