# Generated by Django 4.1.7 on 2023-03-08 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_reservation_alter_dish_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50, unique=True)),
                ('desc_history', models.TextField(max_length=1000)),
            ],
        ),
    ]
