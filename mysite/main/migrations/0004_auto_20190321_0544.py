# Generated by Django 2.0.7 on 2019-03-21 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190312_0336'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='response5',
        ),
    ]