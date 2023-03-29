# Generated by Django 4.1.7 on 2023-03-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_service_alter_about_options_alter_about_desc_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='desc',
            field=models.TextField(max_length=3000, verbose_name='about services'),
        ),
    ]