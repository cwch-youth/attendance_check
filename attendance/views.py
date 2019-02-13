from django.shortcuts import render
from .models import Attendance
from django.contrib.auth.models import User

def attendance_list(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'master'
    user = User.objects.get(username=username)

    attendances = Attendance.objects.filter(user_name=user)
    return render(request, 'attendance/attendance_list.html', {'attends': attendances})
