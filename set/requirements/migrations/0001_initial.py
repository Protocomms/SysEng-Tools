# Generated by Django 2.0.2 on 2020-06-12 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('is_constraint', models.BooleanField(default=False)),
                ('min_measure_of_effectiveness', models.TextField(blank=True, default=None)),
                ('target_measure_of_effectiveness', models.TextField(blank=True, default=None)),
                ('rationale', models.TextField(blank=True, default=None)),
                ('remarks', models.TextField(blank=True, default=None)),
                ('acceptance_criteria_type', models.CharField(blank=True, choices=[('TE', 'Test'), ('DE', 'Demonstrate'), ('AN', 'Analysis')], default=None, max_length=2)),
                ('priority', models.CharField(blank=True, choices=[('MA', 'Mandatory'), ('KE', 'Key Requirement'), ('HI', 'High'), ('ME', 'Medium'), ('LO', 'Low')], default=None, max_length=2)),
                ('status', models.CharField(choices=[('DR', 'Draft'), ('CA', 'Candidate'), ('TR', 'Traded'), ('TF', 'Transferred'), ('CL', 'Cancelled'), ('BA', 'Baselined')], default='DR', max_length=2)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='requirements.Requirement')),
            ],
        ),
    ]