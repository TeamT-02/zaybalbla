# Generated by Django 4.2.3 on 2023-08-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0009_rename_certificat_certificats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=80)),
                ('text', models.TextField()),
            ],
        ),
    ]
