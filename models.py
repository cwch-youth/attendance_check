from django.db import models
from django.utils import timezone

class AttendanceState(object):
    DEFAULT = 0
    ATTEND = 1
    ABSENT = 2
    LATE = 3

# Create your models here.
class Attendance(models.Model):
    user_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    attend_date = models.DateTimeField(default=timezone.now)
    attend_state = models.IntegerField(default=AttendanceState.DEFAULT)

    def __str__(self):
        return '{}: {} {}'.format(self.user_name, self.attend_date, self.attend_state)

    __repr__ = __str__

    def attend(self):
        self.attend_state = AttendanceState.ATTEND

    def absent(self):
        self.attend_state = AttendanceState.ABSENT

    def late(self):
        self.attend_state = AttendanceState.LATE
