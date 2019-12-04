from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=45, unique=True)


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=45, unique=True)
    is_vegetarian = models.IntegerField()
    category = models.ForeignKey(Category, related_name='ingredients', on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % self.ingredient_name

    class Meta:
        ordering = ['ingredient_name']


class Recipe_Type(models.Model):
    recipe_type_id = models.AutoField(primary_key=True)
    recipe_type_name = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % self.recipe_type_name

    class Meta:
        ordering = ['recipe_type_name']


class Beverage(models.Model):
    beverage_id = models.AutoField(primary_key=True)
    beverage_name = models.CharField(max_length=45)
    beverage_type = models.CharField(max_length=45, default='')

    def __str__(self):
        return '%s - %s' % (self.beverage_type, self.beverage_name)

    class Meta:
        ordering = ['beverage_type']


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=45)
    recipe_type = models.ForeignKey(Recipe_Type, related_name='recipes', on_delete=models.PROTECT)
    beverage = models.ForeignKey(Beverage, related_name='recipes', on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % (self.recipe_name)

    class Meta:
        ordering = ['recipe_name']
        unique_together = (('recipe_type', 'recipe_name'))


class Recipe_Ingredient(models.Model):
    recipe_ingredient_id = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredient, related_name='recipe_ingredients', on_delete=models.PROTECT)
    recipe = models.ForeignKey(Recipe, related_name='recipe_ingredients', on_delete=models.PROTECT)


class Beverage_Ingredient(models.Model):
    beverage_ingredient_id = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredient, related_name='beverage_ingredients', on_delete=models.PROTECT)
    beverage = models.ForeignKey(Beverage, related_name='beverage_ingredients', on_delete=models.PROTECT)

