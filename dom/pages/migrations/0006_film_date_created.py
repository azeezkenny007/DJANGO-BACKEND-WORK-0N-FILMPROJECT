# Generated by Django 3.2.12 on 2022-06-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20220606_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]