from django.db import models
from django.utils.translation import gettext as _


class Food(models.Model):
    """The purpose of this class is giving some information about foods"""

    name = models.CharField(_("نام"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=1000)
    rate = models.IntegerField(_("امتیاز"))
    price = models.IntegerField(_("قیمت"), default=0)
    time = models.IntegerField(_("زمان آماده شدن"))
    published_date = models.DateField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    photo = models.ImageField(_("عکس"), upload_to='foods/', blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name