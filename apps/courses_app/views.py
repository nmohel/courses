from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

def index(request):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        Course.objects.create(title=request.POST['title'], desc=request.POST['description'])
    
    return redirect('/courses')

def delete(request, user_id):

    course = Course.objects.get(id=user_id)
    if request.method == 'POST':
        course.delete()
        return redirect('/courses')
    else:
        context = {
            'course': course
        }
        return render(request, 'courses_app/confirm_delete.html', context)
