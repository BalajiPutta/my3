from django.shortcuts import render
from .forms import employeeforms
from .models import employeemodels
def inputdata_view(request):
    if request.method=='POST':
        cform=employeeforms(request.POST)
        if cform.is_valid():
            eno=request.POST.get('eno')
            ename=request.POST.get('ename')
            eposition=request.POST.get('eposition')
            eaddress=request.POST.get('eaddress')
            eproject=request.POST.get('eproject')
            esalary=request.POST.get('esalary')
            eusername=request.POST.get('eusername')
            epassword=request.POST.get('epassword')
            eemail=request.POST.get('eemail')
            data=employeemodels(eno=eno,ename=ename,epassword=epassword,eemail=eemail,eusername=eusername,esalary=esalary,eproject=eproject,eaddress=eaddress,eposition=eposition)
            data.save()
            cform =employeeforms()
            return render(request, 'test.html', {'cform': cform})
    else:
        cform=employeeforms()
        return render(request,'test.html',{'cform':cform})
