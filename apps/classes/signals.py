from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import CourseSchedule, Class
from django.core.exceptions import ValidationError

@receiver(pre_save, sender=CourseSchedule)
def trigger_order_processing(sender, instance, **kwargs):
    courseSchedule = CourseSchedule.objects.filter(day_of_week=instance.day_of_week, _class=instance._class).exclude(id=instance.id)
    for c in courseSchedule:
        if instance.start_time < c.end_time and instance.end_time > c.start_time:
            raise ValidationError("Conflict in Schedule!")
