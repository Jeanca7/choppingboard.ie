# Generated by Django 2.0.8 on 2018-11-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipe_cook'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
