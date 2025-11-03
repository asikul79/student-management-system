from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def home(request):
    return render(request, 'myapp/home.html')

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)  
        if form.is_valid():                
            form.save()                    
            return redirect('display_student')
    else:
        form = StudentForm()               

    return render(request, 'myapp/add_student.html', {'form': form})

def display_student(request):
    students = Student.objects.all()
    return render(request, 'myapp/display_student.html', {'students': students})

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('display_student')
    else:
        form = StudentForm(instance=student)
    return render(request, 'myapp/update_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('display_student')
    return render(request, 'myapp/delete_student.html', {'student': student})
