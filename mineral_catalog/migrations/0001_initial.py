# Generated by Django 2.1.3 on 2018-12-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_filename', models.CharField(max_length=100)),
                ('image_caption', models.CharField(blank=True, max_length=100)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('formula', models.CharField(blank=True, max_length=100)),
                ('strunz_classification', models.CharField(blank=True, max_length=100)),
                ('crystal_system', models.CharField(blank=True, max_length=100)),
                ('unit_cell', models.CharField(blank=True, max_length=100)),
                ('color', models.CharField(blank=True, max_length=100)),
                ('crystal_symmetry', models.CharField(blank=True, max_length=100)),
                ('cleavage', models.CharField(blank=True, max_length=100)),
                ('mohs_scale_hardness', models.CharField(blank=True, max_length=100)),
                ('luster', models.CharField(blank=True, max_length=100)),
                ('streak', models.CharField(blank=True, max_length=100)),
                ('diaphaneity', models.CharField(blank=True, max_length=100)),
                ('optical_properties', models.CharField(blank=True, max_length=100)),
                ('refractive_index', models.CharField(blank=True, max_length=100)),
                ('crystal_habit', models.CharField(blank=True, max_length=100)),
                ('specific_gravity', models.CharField(blank=True, max_length=100)),
                ('group', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
