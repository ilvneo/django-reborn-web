# Generated by Django 3.0.2 on 2020-02-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0006_auto_20200204_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymous',
            name='comments',
            field=models.PositiveIntegerField(default='0', verbose_name='댓글수'),
        ),
    ]