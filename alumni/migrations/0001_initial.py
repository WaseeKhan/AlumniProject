# Generated by Django 3.1.2 on 2020-10-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('batch', models.IntegerField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('portal_join_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('cur_status', models.CharField(max_length=100, null=True)),
                ('cur_address', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
