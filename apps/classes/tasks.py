from celery import shared_task
from .models import Class, Course, CourseSchedule 

@shared_task
def update_class_status():
    from django.utils.timezone import localtime, now
    _time = localtime(now())
    current_day = _time.isoweekday() % 7 + 2
    current_time = _time.time()

    Class.objects.update(in_use=False)

    active_schedules = CourseSchedule.objects.filter(day_of_week=current_day, start_time__lte=current_time, end_time__gte=current_time).prefetch_related('_class')

    for schedule in active_schedules:
        class_obj = schedule._class
        class_obj.in_use = True
        class_obj.save(update_fields=["in_use"])