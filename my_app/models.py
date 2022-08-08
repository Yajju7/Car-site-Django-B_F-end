from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.  
class Patient(models.Model):
    p_fname = models.CharField(max_length=30)
    p_lname = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MaxValueValidator(150)])
    heart_rate = models.IntegerField(default=60, validators=[MinValueValidator(1), MaxValueValidator(300)])
    
    
    def __str__(self):
        return f"{id} The first name is {self.p_fname} and last name is {self.p_lname} and age is {self.age}. His heart rate is {self.heart_rate} "