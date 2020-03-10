# Generated by Django 3.0.2 on 2020-03-10 18:42

from django.db import migrations, models
import notice.models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0017_auto_20200303_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='free',
            name='files',
        ),
        migrations.AddField(
            model_name='free',
            name='upload_images',
            field=models.FileField(blank=True, null=True, upload_to=notice.models.get_file_path, verbose_name='이미지파일'),
        ),
        migrations.AlterField(
            model_name='free',
            name='upload_files',
            field=models.FileField(blank=True, null=True, upload_to=notice.models.get_file_path, verbose_name='파일'),
        ),
    ]
