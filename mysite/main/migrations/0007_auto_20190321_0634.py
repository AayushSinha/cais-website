# Generated by Django 2.0.7 on 2019-03-21 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190321_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserResponse',
        ),
    ]
