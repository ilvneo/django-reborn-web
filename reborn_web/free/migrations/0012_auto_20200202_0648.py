# Generated by Django 3.0.2 on 2020-02-01 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0011_auto_20200202_0303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '자유게시판 댓글', 'verbose_name_plural': '자유게시판 댓글'},
        ),
        migrations.AlterModelTable(
            name='comment',
            table='자유게시판 댓글',
        ),
    ]