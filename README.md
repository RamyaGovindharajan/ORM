# Ex02 Django ORM Web Application
## Date: 28/10/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-10-28 155559.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

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

admin.py


from django.contrib import admin
from .models import bankloan, bankloanAdmin  
admin.site.register(bankloan,bankloanAdmin)

```

## OUTPUT
![alt text](<Screenshot 2024-10-28 154106.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
