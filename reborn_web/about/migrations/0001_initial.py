# Generated by Django 3.0.2 on 2020-03-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circles_name', models.CharField(max_length=8, verbose_name='동아리이름')),
                ('introduce', models.TextField(verbose_name='동아리소개')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '동아리소개',
                'verbose_name_plural': '동아리소개',
                'db_table': '동아리소개',
            },
        ),
        migrations.CreateModel(
            name='Labs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labs_name', models.CharField(max_length=8, verbose_name='연구실이름')),
                ('location', models.CharField(max_length=8, verbose_name='연구실위치')),
                ('introduce', models.TextField(verbose_name='연구실소개')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '연구실소개',
                'verbose_name_plural': '연구실소개',
                'db_table': '연구실소개',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='이름')),
                ('department', models.CharField(max_length=10, verbose_name='부서')),
                ('rank', models.CharField(choices=[('회장', '회장'), ('부회장', '부회장'), ('부장', '부장'), ('차장', '차장'), ('부원', '부원')], max_length=10, verbose_name='직급')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '학생회조직도',
                'verbose_name_plural': '학생회조직도',
                'db_table': '학생회조직도',
            },
        ),
    ]