from django.db import models

# Create your models here.

class Password(models.Model):
	password = models.CharField(max_length=50, null = False)


	def __str__(self):
		return self.password

	class Meta:
		verbose_name = 'Parol'

class Employees(models.Model):
	name = models.CharField(max_length = 100, null = True, blank=True)
	first_name = models.CharField(max_length=100, null= True, blank=True)
	birthday = models.CharField(max_length=50, null=True, blank=True)
	contact = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Xodimlar'


class Reports(models.Model):
	parent = models.ForeignKey(Employees,on_delete=models.CASCADE)
	report = models.CharField(max_length=20, null=True, blank=False, verbose_name = 'Zayavkalar soni')
	called = models.CharField(max_length=20, null=True, blank=True, verbose_name= 'Gaplashildi')
	sells =  models.CharField(max_length=20, null=True, blank=True, verbose_name="Sotilgan masulotlar")
	no_called = models.CharField(max_length=20, null=True, blank=True, verbose_name = "Teliga tushib bo'lmaganlar soni")
	error_num = models.CharField(max_length=20, null=True, blank=True, verbose_name = "Noto'g'ri raqamlar")
	number_x = models.CharField(max_length=20, null=True, blank=True, verbose_name="Otkazlar soni")
	report_x = models.CharField(max_length=20, null=True, blank=True, verbose_name="Buyutma bermagan yoki adashganlar")
	cash_pay = models.CharField(max_length=20, null=True, blank=True, verbose_name="Naqd to'lovlar soni")
	click_pay = models.CharField(max_length=20, null=True, blank=True, verbose_name="Click orqali to'lovlar soni")
	other_pay = models.CharField(max_length=20, null=True, blank=True, verbose_name="Boshqa usuldagi to'lovlar")
	special_pay = models.CharField(max_length=20, null=True, blank=True, verbose_name="Maxsus narxda sotilgan mahsulotlar")
	donation = models.CharField(max_length=20, null=True, blank=True, verbose_name="Ehsonlar soni")
	num_customer = models.CharField(max_length=20, null=True, blank=True, verbose_name="Sotib olgan mijozlar soni")
	money = models.CharField(max_length=20, null=True, blank=False, verbose_name = "Summa")

	class Meta:
		verbose_name = "Hisobotlar"

