from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# class Length(models.Model):
#     length = models.PositiveIntegerField(validators=[MinValueValidator(160), MaxValueValidator(190)])
    
#     def __str__(self):
#         return (self.length)
        
# class Type(models.Model):
#     type = models.CharField(max_length=20)

#     def __str__(self):
#         return (self.type) 

# class AbilityLevel(models.Model):
#     level = models.CharField(max_length=20)

    # def __str__(self):
    #     return (self.level)
class Skis(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    waistwidth = models.PositiveIntegerField(validators=[MinValueValidator(50), MaxValueValidator(150)])
    type = models.CharField(max_length=100)
    length = models.PositiveIntegerField(default=150)
    # type = models.ForeignKey(Type, on_delete=models.CASCADE)
    # length = models.ManyToManyField(Length, blank=True)
    # ability = models.ManyToManyField(AbilityLevel, blank=True)

    def __str__(self):
        return (self.model)

