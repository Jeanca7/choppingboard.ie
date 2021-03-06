# Generated by Django 2.0.8 on 2019-02-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_recipe_users_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
