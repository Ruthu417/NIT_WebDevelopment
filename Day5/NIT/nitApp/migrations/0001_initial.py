# Generated by Django 3.2 on 2024-12-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erl', models.CharField(max_length=12)),
                ('en', models.CharField(max_length=150)),
                ('es', models.IntegerField(default=10)),
            ],
        ),
    ]
