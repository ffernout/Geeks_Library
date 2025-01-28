from django.db import models





class RecipeListView(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    CHOICES = (
        ('Граммы', 'Граммы'),
        ('Килограммы', 'Килограммы'),
        ('Миллилитры', 'Миллилитры'),
    )

    name = models.TextField()
    quantity = models.IntegerField()
    unit = models.CharField(max_length= 100, choices=CHOICES)
    recipe = models.ForeignKey(Recipe, max_length= 100, choices=CHOICES, related_name='ingredients',)

    def __str__(self):
        return self.name
