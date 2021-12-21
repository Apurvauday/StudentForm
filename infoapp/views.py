from django.shortcuts import render
from infoapp.forms import StudentModelForm

# Create your views here.
def student_view(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print()
            student_list = Student.objects.all()
            student_dict = {'student_list': student_list}
    return render(request,'infoapp/student.html',context=student_dict)
