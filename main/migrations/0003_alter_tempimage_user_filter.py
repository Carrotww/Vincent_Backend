# Generated by Django 4.1.3 on 2022-11-24 13:44

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_tempimage_temp_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempimage',
            name='user_filter',
            field=models.ImageField(null=True, upload_to=main.utils.rename_imagefile_to_uuid),
        ),
    ]
