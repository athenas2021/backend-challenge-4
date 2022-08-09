from django.db import models


class Revenue(models.Model):
    description = models.CharField(max_length=100, blank=False)
    value = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    date = models.DateField(auto_now_add=False, blank=False)

    def __str__(self) -> str:
        return (f'{self.date} ${self.value} - {self.description[:15]}...')
