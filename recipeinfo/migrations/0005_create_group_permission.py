from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    category_view_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                         content_type__model='category',
                                                         codename='view_category')

    category_add_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                        content_type__model='category',
                                                        codename='add_category')

    ingredient_view_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                           content_type__model='ingredient',
                                                           codename='view_ingredient')

    ingredient_add_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                          content_type__model='ingredient',
                                                          codename='add_ingredient')

    recipe_type_view_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                            content_type__model='recipe_type',
                                                            codename='view_recipe_type')

    recipe_type_add_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                           content_type__model='recipe_type',
                                                           codename='add_recipe_type')

    dessert_view_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                        content_type__model='dessert',
                                                        codename='view_dessert')

    dessert_all_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                       content_type__model='dessert')

    beverage_view_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                         content_type__model='beverage',
                                                         codename='view_beverage')

    beverage_all_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                        content_type__model='beverage')

    recipe_view_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                       content_type__model='recipe',
                                                       codename='view_recipe')

    recipe_all_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                      content_type__model='recipe')

    recipe_ingredient_all_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                                 content_type__model='recipe_ingredient')

    beverage_ingredient_all_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                                   content_type__model='beverage_ingredient')

    dessert_ingredient_all_perm = permission_class.objects.filter(content_type__app_label='recipeinfo',
                                                                  content_type__model='dessert_ingredient')

    ri_recipe_developer_permissions = chain(category_add_perm, category_view_perm, ingredient_view_perm,
                                            ingredient_add_perm, recipe_type_view_perm, recipe_type_add_perm,
                                            dessert_view_perm, beverage_view_perm, recipe_all_perm,
                                            recipe_ingredient_all_perm)

    ri_beverage_developer_permissions = chain(category_view_perm, ingredient_view_perm, ingredient_add_perm,
                                              dessert_view_perm, beverage_all_perm, recipe_view_perm,
                                              beverage_ingredient_all_perm)

    ri_dessert_developer_permissions = chain(category_view_perm, ingredient_view_perm, ingredient_add_perm,
                                             recipe_type_view_perm, dessert_all_perm, beverage_view_perm,
                                             recipe_view_perm, dessert_ingredient_all_perm)

    my_groups_initialization_list = [
        {
            "name": "ri_recipe_developer",
            "permissions_list": ri_recipe_developer_permissions,
        },
        {
            "name": "ri_beverage_developer",
            "permissions_list": ri_beverage_developer_permissions,
        },
        {
            "name": "ri_dessert_developer",
            "permissions_list": ri_dessert_developer_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name = group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('recipeinfo', '0004_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
