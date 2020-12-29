# Generated by Django 3.1.4 on 2020-12-29 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical_records', '0012_update_related_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonpathologicalbackground',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='non_pathological_background', related_query_name='non_pathological_background', to='medical_records.patient'),
        ),
    ]