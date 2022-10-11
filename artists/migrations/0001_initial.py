# Generated by Django 4.1.2 on 2022-10-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stageName', models.CharField(max_length=100, unique=True)),
                ('socialMediaProfile', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['stageName'],
            },
        ),
    ]