from django.db import models
from django.core.validators import RegexValidator # Для регулних виразів

# Create your models here.
class DishCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        for dish in self.dishes.filter(is_visible=True):
            yield dish

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Dish(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, related_name='dishes', on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    is_signature = models.BooleanField(default=False)
    desc = models.TextField(max_length=200, blank=True, verbose_name='about dish')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    ingredients = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dishes')
    is_recommended = models.BooleanField(default=False)

    def total_price(self):
        return self.price - self.discount / 100 * self.price

    class Meta:
        ordering = ('position',)
        verbose_name = 'Dish'
        verbose_name_plural = "Dishes"

    def __str__(self):
        return f'{self.title}'


class Reservation(models.Model):
    phone_validator = RegexValidator(regex='^\+?3?8?0?\d{2}[ -]?(\d[ -]?){7}$',
                                     message='Phone number is waited in format +380xx xxx xx xx')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=16, validators=(phone_validator,))
    visit_datetime = models.DateField()
    date_request = models.DateTimeField(auto_now_add=True)
    date_response = models.DateTimeField(auto_now=True)
    guests = models.CharField(max_length=10)
    message = models.TextField(max_length=1000, blank=True)
    is_processed = models.BooleanField(default=False)



    class Meta:
        ordering = ('-date_request', )

    def __str__(self):
        return f'{self.name}\t{self.phone}\t{self.email}'

class About(models.Model):
    heading = models.CharField(max_length=50, unique=True)
    desc_history = models.TextField(max_length=3000)


    class Meta:
        verbose_name = 'About'
        verbose_name_plural = "Abouts"

    def __str__(self):
        return f'{self.heading}\t{self.desc_history}'


class Service(models.Model):
    icon_choices = [
        ("H", " heart"),
        ("T", "user-tie"),
        ("HAM", "hamburger")
    ]

    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    desc = models.TextField(max_length=3000, verbose_name='about services')
    is_visible = models.BooleanField(default=True)
    icon = models.CharField(max_length=3, choices=icon_choices, default="H")

    class Meta:
        ordering = ('position',)
        verbose_name = 'Service'
        verbose_name_plural = "Services"

    def __str__(self):
        return f'{self.title}'

class Gallery(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f'{self.title}'

