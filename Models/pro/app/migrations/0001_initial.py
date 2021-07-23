# Generated by Django 3.2.5 on 2021-07-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=15)),
            ],
        ),
    ]