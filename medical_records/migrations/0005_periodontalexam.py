# Generated by Django 3.0.8 on 2020-08-01 05:03

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medical_records', '0004_medicalbackground'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodontalExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('dental_plaque', models.BooleanField(default=False)),
                ('calculus', models.BooleanField(default=False)),
                ('bleeding', models.BooleanField(default=False)),
                ('tooth_mobility', models.BooleanField(default=False)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='medical_records.Patient')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
