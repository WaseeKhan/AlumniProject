# Generated by Django 3.1.2 on 2020-10-05 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_auto_20201005_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addalumni',
            name='batch',
            field=models.IntegerField(null=True),
        ),
    ]