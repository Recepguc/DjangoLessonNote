from itertools import combinations_with_replacement
from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm


def index(request):
    return render(request, 'fscohort/index.html')


def student_list(request):
    student = Student.objects.all()

    context = {
        "students": student
    }
    return render(request, "fscohort/student_list.html", context)


def student_add(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")

    context = {
        "form": form
    }

    return render(request, "fscohort/student_add.html", context)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)

    context = {
        "form": form
    }
    return render(request, "fscohort/student_update.html", context)
