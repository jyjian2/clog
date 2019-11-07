from django.db import models


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.ingredient_name

    class Meta:
        ordering = ['ingredient_name']



class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=45)
    recipe_type = models.CharField(max_length=45, default="Temporary")

    def __str__(self):
        return '%s - %s' % (self.recipe_type, self.recipe_name)

    class Meta:
        ordering = ['recipe_type']
        unique_together = (('recipe_type', 'recipe_name'))


class Recipe_Ingredient(models.Model):
    recipe_ingredient_id = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredient, related_name='recipe_ingredients', on_delete=models.PROTECT)
    recipe = models.ForeignKey(Recipe, related_name='recipe_ingredients', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.ingredient, self.recipe.recipe_name)

    class Meta:
        ordering = ['ingredient']
        unique_together = (('ingredient', 'recipe'))






