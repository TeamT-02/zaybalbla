# Generated by Django 4.2.3 on 2023-08-03 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0012_alter_factory_about_videofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory_about',
            name='videofile',
            field=models.FileField(null=True, upload_to='midea/video/'),
        ),
    ]
