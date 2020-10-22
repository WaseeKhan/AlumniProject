# Generated by Django 3.1.2 on 2020-10-09 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0010_auto_20201006_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, upload_to='SlidePics/')),
            ],
        ),
    ]
