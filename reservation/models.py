from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Reservation(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=100, blank=False)
    email = models.EmailField(_("آدرس الکترونیکی"), max_length=100)
    phone = models.CharField(_("تلفن"), max_length=20, blank=False)
    number = models.IntegerField(_("تعداد"), default=1)
    date = models.DateField(_("تاریخ"), auto_now=False, auto_now_add=False)
    time = models.DateTimeField(_("ساعت"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
