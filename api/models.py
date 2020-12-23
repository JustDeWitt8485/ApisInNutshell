from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=200)


class ShoeType(models.Model):
    style = models.CharField(max_length=50)


class ShoeColor(models.Model):
    RED = 'R'
    ORANGE = 'O'
    YELLOW = 'Y'
    GREEN = 'G'
    BLUE = 'B'
    INDIGO = 'I'
    VIOLET = 'V'
    BLACK = 'BL'
    WHITE = 'W'

    COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (BLACK, 'Black'),
        (WHITE, 'White'),
    ]
    color_name = models.CharField(
        max_length=2,
        choices=COLOR_CHOICES,
        default=WHITE
    )


class Shoe(models.Model):
    VELCRO = 'V'
    SHOE_LACES = 'SL'

    FASTEN_CHOICES = [
        (VELCRO, 'Velcro'),
        (SHOE_LACES, 'Shoe_Laces')
    ]

    size = models.IntegerField(default=1)
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(
        max_length=2,
        choices=FASTEN_CHOICES,
        default=SHOE_LACES
    )
