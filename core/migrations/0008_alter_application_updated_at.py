# Generated by Django 5.0.6 on 2024-12-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_application_application_unique_application_per_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='updated_at',
            field=models.DateField(null=True),
        ),
    ]
