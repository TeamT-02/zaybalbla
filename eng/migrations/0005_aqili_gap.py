# Generated by Django 4.2.3 on 2023-07-31 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0004_rename_about_about_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aqili_gap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256)),
                ('job_nmae', models.CharField(max_length=256)),
                ('text', models.TextField(max_length=150)),
                ('image', models.ImageField(upload_to='midea/avatar/')),
            ],
        ),
    ]