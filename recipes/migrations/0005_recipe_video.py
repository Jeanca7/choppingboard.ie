# Generated by Django 2.0.8 on 2018-11-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_remove_recipe_videofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='video',
            field=models.FileField(null=True, upload_to='videos'),
        ),
    ]
