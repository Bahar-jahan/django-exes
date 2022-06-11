from django.db import models

# Create your models here.


class FoodGroup(models.Model):
    group_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=100000, default='https://th.bing.com/th/id/R.048fe00ae936f5b1ceef950ff314271d?rik=PPn3NcFhqZ46IA&riu=http%3a%2f%2fwww.vgmpf.com%2fWiki%2fimages%2fc%2fcb%2fNoPhoto.png&ehk=h28ESegf6decjqYgG7NuE1ZQ02oar%2bryghpicALBdeI%3d&risl=&pid=ImgRaw&r=0', null=True, blank=True)
    url = models.CharField(
        max_length=50, default='index', null=True, blank=True)

    def __str__(self):
        return self.group_name


class Food(models.Model):
    food_group = models.ForeignKey(
        FoodGroup, on_delete=models.CASCADE, null=True)
    food_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    image = models.CharField(max_length=100000, default='https://th.bing.com/th/id/R.048fe00ae936f5b1ceef950ff314271d?rik=PPn3NcFhqZ46IA&riu=http%3a%2f%2fwww.vgmpf.com%2fWiki%2fimages%2fc%2fcb%2fNoPhoto.png&ehk=h28ESegf6decjqYgG7NuE1ZQ02oar%2bryghpicALBdeI%3d&risl=&pid=ImgRaw&r=0', null=True, blank=True)

    def __str__(self):
        return f"{self.food_name}\t\t\t{self.price} "
