# Generated by Django 4.1.7 on 2023-03-07 16:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_dishcategory_options_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Phone number is waited in format +380xx xxx xx xx', regex='^+?3?8?0?\\{2}[- ]?(\\d[ -]?){7}$')])),
                ('date', models.DateTimeField()),
                ('date_request', models.DateTimeField(auto_now_add=True)),
                ('date_response', models.DateTimeField(auto_now=True)),
                ('guests', models.PositiveSmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=1000)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date_request',),
            },
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('position',), 'verbose_name': 'Dish', 'verbose_name_plural': 'Dishes'},
        ),
        migrations.AlterModelOptions(
            name='dishcategory',
            options={'ordering': ('position',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='main_app.dishcategory'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='desc',
            field=models.TextField(blank=True, max_length=200, verbose_name='about dish'),
        ),
    ]
