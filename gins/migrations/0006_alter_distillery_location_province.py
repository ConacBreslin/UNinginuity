# Generated by Django 3.2.8 on 2021-10-31 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gins', '0005_auto_20211031_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distillery',
            name='location_province',
            field=models.CharField(blank=True, default='Ulster', max_length=10, null=True),
        ),
    ]