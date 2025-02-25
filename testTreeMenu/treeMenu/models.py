from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_items(self):
        # Получаем все элементы меню, включая дочерние элементы
        return self.items.filter(parent=None).order_by('order')


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200, blank=True, null=True)
    named_url = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url

    def __str__(self):
        return self.title

