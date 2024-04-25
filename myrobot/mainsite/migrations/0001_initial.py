# Generated by Django 3.2.13 on 2022-12-20 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('lng_lat', models.CharField(max_length=50)),
                ('entry_method', models.CharField(max_length=200)),
                ('source_type', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=400)),
            ],
        ),
    ]
