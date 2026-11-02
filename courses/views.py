from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Course, Enrollment


# Create your views here.
@login_required
def course_list(request):
    courses=Course.objects.all()

    enrolled_courses = Enrollment.objects.filter(
        student=request.user
    ).values_list('course_id', flat=True)

    return render(
    request,
    'courses/course_list.html',
    {
        'courses': courses,
        'enrolled_courses': enrolled_courses
    }
)

@login_required
def course_detail(request,course_id):
    course=get_object_or_404(Course,id=course_id)
    is_enrolled = Enrollment.objects.filter(
    student=request.user,
    course=course
    ).exists()
    return render(
    request,
    'courses/course_detail.html',
    {
        'course': course,
        'is_enrolled': is_enrolled
    }
)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        print("Login username:", repr(username))
        print("Password received:", bool(password))

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("Authentication result:", user)

        if user is not None:
            login(request, user)
            return redirect('course_list')

        return render(
            request,
            'courses/login.html',
            {'error': 'Invalid username or password'}
        )

    return render(request, 'courses/login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'courses/register.html',
                {'error':'Username already exists'}

            )
    
        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request,'courses/register.html')


def user_logout(request):
    if request.method == 'POST':    
        logout(request)
        return redirect('login')
    return redirect('course_list')

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course,id=course_id)

    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    return redirect('my_courses')

@login_required
def my_courses(request):
    enrollments=Enrollment.objects.filter(
        student=request.user
    ).select_related('course')

    return render(
        request,
        'courses/my_courses.html',
        {'enrollments':enrollments}
    )
