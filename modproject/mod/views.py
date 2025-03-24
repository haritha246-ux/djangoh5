from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import Student
def add_student(request):
  student = Student(name="John Doe", age=22, email="johndoe@example.com")
  student.save()
  return HttpResponse("Student record added successfully!")
def student_list(request):
   students = Student.objects.all()
   return render(request, 'mod/std.html', {'students': students})

