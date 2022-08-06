# Generated by Django 4.1 on 2022-08-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField()),
            ],
        ),
    ]
