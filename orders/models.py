from django.db import models
from django.db.models.base import Model
from django.urls import reverse, reverse_lazy
from uuslug import uuslug as slugify

from django.utils.translation import gettext_lazy as _
from random import randint


class Goods(models.Model):
    name = models.CharField(verbose_name=_("name of goods"), max_length=256)
    description = models.CharField(
        verbose_name=_("description of goods"), max_length=256
    )
    manufacturer = models.CharField(
        verbose_name=_("manufacturer of goods"), max_length=256
    )
    slug = models.SlugField(blank=True, unique=True)
    price = models.IntegerField(
        verbose_name=_("price of goods"),
    )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        slug_str = "%s %s %s %s" % (self.pk, "-", self.price, self.name)
        self.slug = slugify(slug_str, instance=self)
        return super().save(*args, **kwargs)


class Orders(models.Model):
    date = models.DateField(verbose_name=_("date of order"), auto_now=True)
    counter_party = models.CharField(
        verbose_name=_("counter party of order"), max_length=256
    )
    slug = models.SlugField(blank=True, unique=True)
    quantity = models.IntegerField(verbose_name=_("quantity of order"), max_length=1000)
    goods = models.ForeignKey(
        Goods, on_delete=models.CASCADE, verbose_name=_("order goods")
    )

    def __str__(self) -> str:
        return self.counter_party

    def get_absolute_url(self):
        return reverse_lazy("order-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        slug_str = "%s %s %s" % (self.pk, self.quantity, self.counter_party)
        self.slug = slugify(slug_str, instance=self)
        return super(Orders, self).save(*args, **kwargs)
