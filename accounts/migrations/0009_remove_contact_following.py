# Generated by Django 2.0.8 on 2019-02-05 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_contact_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='following',
        ),
    ]
