from django.db import models


from datetime import datetime, timezone






class customer(models.Model):
    
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)


class record(models.Model):
    
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    remark = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)



class payment(models.Model):
    
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(auto_now=False)
    remark = models.CharField(max_length=50, null=True, blank=True)
