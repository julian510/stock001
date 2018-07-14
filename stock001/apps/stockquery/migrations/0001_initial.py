# Generated by Django 2.0.7 on 2018-07-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock_data',
            fields=[
                ('index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=50)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('volume', models.FloatField()),
                ('code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('nameid', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, null=True, unique=True)),
                ('passwd', models.CharField(max_length=50)),
                ('chiname', models.CharField(max_length=50)),
                ('phnum', models.CharField(max_length=50)),
                ('email', models.EmailField(default=None, max_length=100)),
            ],
        ),
    ]