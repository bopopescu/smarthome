# Generated by Django 2.0.7 on 2018-07-12 07:50

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intent', models.TextField(max_length=64)),
                ('slots', models.TextField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Nodedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField(max_length=64)),
                ('localshortaddr', models.TextField(max_length=64)),
                ('gateway_id', models.TextField(max_length=64)),
                ('subordinateId', models.TextField(max_length=64)),
                ('humidity', models.IntegerField(default=0)),
                ('temperature', models.IntegerField(default=0)),
                ('light', models.IntegerField(default=0)),
                ('noise', models.IntegerField(default=0)),
                ('co2_simulation', models.IntegerField(default=0)),
                ('co2_binarization', models.IntegerField(default=0)),
            ],
        ),
    ]
