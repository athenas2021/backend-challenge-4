from django.db import models


class Expenditure(models.Model):

    CATEGORIES_CHOICES = (
        (1, 'food'),
        (2, 'health'),
        (3, 'home'),
        (4, 'transport'),
        (5, 'education'),
        (6, 'leisure'),
        (7, 'unforeseen'),
        (8, 'food'),
    )

    description = models.CharField(max_length=100, blank=False)
    value = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    date = models.DateField(auto_now_add=False, blank=False)
    category = models.IntegerField('category', choices=CATEGORIES_CHOICES, default=8)

    def __str__(self) -> str:
        return (f'{self.date} ${self.value} - {self.description[:15]}...')
