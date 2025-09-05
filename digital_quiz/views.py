from django.shortcuts import render, redirect
from .models import Student, Question, Response

def dashboard(request):
    questions = Question.objects.all()
    if request.method == "POST":
        gender = request.POST.get("gender")
        student = Student.objects.create(gender=gender)

        for q in questions:
            selected = request.POST.get(f"q{q.id}")
            time_taken = request.POST.get(f"time_q{q.id}") or 0
            if selected:
                Response.objects.create(
                    participant=student,
                    question=q,
                    selected_option=selected,
                    time_taken=float(time_taken),
                )
        return redirect("thank_you")  # make a simple "Thank You" page

    return render(request, "dashboard.html", {"questions": questions})

def thank_you(request):
    return render(request, "thank.html")