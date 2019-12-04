# Generated by Django 2.2.5 on 2019-12-04 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('beverage_id', models.AutoField(primary_key=True, serialize=False)),
                ('beverage_name', models.CharField(max_length=45)),
                ('beverage_type', models.CharField(default='Temporary', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Beverage_Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredient_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=45, unique=True)),
                ('is_vegetarian', models.IntegerField()),
            ],
            options={
                'ordering': ['ingredient_name'],
            },
        ),
        migrations.CreateModel(
            name='Recipe_Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('recipe_name', models.CharField(max_length=45)),
                ('recipe_type', models.CharField(default='Temporary', max_length=45)),
            ],
            options={
                'ordering': ['recipe_type'],
                'unique_together': {('recipe_type', 'recipe_name')},
            },
        ),
    ]