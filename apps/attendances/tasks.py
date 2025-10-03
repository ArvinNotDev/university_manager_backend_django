from celery import shared_task
from django.utils.timezone import localtime, now
from classes.models import CourseSchedule
from .models import AttendanceSession


@shared_task
def create_attendance_sessions():
    _time = localtime(now())
    current_day = _time.isoweekday() % 7 + 2
    current_time = _time.time()

    active_schedules = CourseSchedule.objects.filter(
        day_of_week=current_day,
        start_time__lte=current_time,
        end_time__gte=current_time,
        is_active=True
    ).select_related("course")

    for schedule in active_schedules:
        course = schedule.course
        for class_obj in course._class.all():
            already_exists = AttendanceSession.objects.filter(course=course, class_obj=class_obj, schedule=schedule, created_at__date=_time.date()).exists()
            if not already_exists:
                AttendanceSession.objects.create(
                    course=course,
                    class_obj=class_obj,
                    schedule=schedule
                )
