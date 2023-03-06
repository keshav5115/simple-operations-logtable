from django.db import models

# Create your models here.
class LogTable(models.Model):
    numbers=[['zero','zero'],['one','one'],['two','two'],['three','three'],['four','four'],['five','five'],['six','six'],['seven','seven'],['eight','eight'],['nine','nine']]
    operand1=models.CharField(max_length=10,choices=numbers)
    oper=[['plus','plus'],['minus','minus'],['times','times'],['divided_by','divided_by']]
    operator=models.CharField(max_length=20,choices=oper)
    operand2=models.CharField(max_length=10,choices=numbers)
    output=models.IntegerField()