from django.db import models
from django.contrib import admin
class bankloan(models.Model):
	Name=models.CharField(max_length=30 )
	Account_no=models.IntegerField(primary_key=True)
	Loan_amount=models.IntegerField()
	Interest_amount=models.FloatField()
	DOB=models.DateField()
class bankloanAdmin(admin.ModelAdmin):
	list_display=("Name","Account_no","Loan_amount","Interest_amount","DOB")