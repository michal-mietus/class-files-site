# Generated by Django 2.1.7 on 2019-02-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='icon_name',
            field=models.CharField(default='icon.png', max_length=30),
            preserve_default=False,
        ),
    ]
