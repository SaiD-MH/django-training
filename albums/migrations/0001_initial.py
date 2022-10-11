# Generated by Django 4.1.2 on 2022-10-11 17:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Album', max_length=60)),
                ('creationTime', models.DateTimeField(default=datetime.datetime.now)),
                ('release', models.DateTimeField(default=datetime.datetime.now)),
                ('cost', models.DecimalField(decimal_places=5, default=0.0, max_digits=10)),
                ('artistName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.artist')),
            ],
        ),
    ]