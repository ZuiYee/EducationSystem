# Generated by Django 2.1.4 on 2018-12-05 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_classtable_classcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='teacher',
            new_name='teacherName',
        ),
        migrations.RenameField(
            model_name='classtable',
            old_name='teacher',
            new_name='teacherName',
        ),
    ]
