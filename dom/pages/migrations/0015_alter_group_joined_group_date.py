# Generated by Django 3.2.12 on 2023-01-19 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_alter_group_joined_group_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='joined_group_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 1, 19), null=True),
        ),
    ]
