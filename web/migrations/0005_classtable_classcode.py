# Generated by Django 2.1.4 on 2018-12-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='classtable',
            name='classCode',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='课程代码'),
        ),
    ]
