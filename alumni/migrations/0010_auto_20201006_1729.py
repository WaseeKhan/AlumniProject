# Generated by Django 3.1.2 on 2020-10-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0009_auto_20201006_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addalumni',
            name='dp',
            field=models.ImageField(null=True, upload_to='dp/'),
        ),
        migrations.AlterField(
            model_name='addalumni',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]