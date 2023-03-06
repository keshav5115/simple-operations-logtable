from django.shortcuts import render
from django.http import HttpResponse
from app.forms import LogTable,CalForm
# Create your views here.
def zero():
    return 0
def one():
    return 1
def two():
    return 2
def three():
    return 3
def four():
    return 4
def five():
    return 5
def  six():
    return 6
def seven():
    return 7
def eight():
    return 8
def nine():
    return 9

operands={
    'zero':zero,
    'one':one,
    'two':two,
    'three':three,
    'four':four,
    'five':five,
    'six':six,
    'seven':seven,
    'eight':eight,
    'nine':nine,
}

def calculation(request):
    form =CalForm()
    output=''
    try:
        if request.method=='POST':
            oper1=request.POST['operand1']
            oper2=request.POST['operand2']
            operand1=operands[oper1]
            operand2=operands[oper2]
            operator=request.POST['operator']
            if operator =='plus':
                output=operand1()+operand2()
            elif operator =='minus':
                output=operand1()-operand2()
            elif operator =='times':
                output=operand1()*operand2()
            elif operator =='divided_by':
                output=operand1()//operand2()
            LogTable.objects.create(operand1=oper1,operator=operator,operand2=oper2,output=output)
    except:
        return HttpResponse('enter valid data')
    return render(request,'calculation.html',{'form':form,'output':output})

def LogTableVW(request):
    data=LogTable.objects.all()
    return render(request,'logtable.html',{'data':data})