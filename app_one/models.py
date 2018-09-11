from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Task(models.Model):
    work_name = models.TextField(max_length=256)
    starting_date = models.DateField(default=timezone.now())
    ending_date = models.DateField(default=timezone.now())
    work_status = models.TextField(max_length=256)

    def __str__(self):
        return self.work_name

    def get_absolute_url(self):
        return reverse("app_one:task_list")  # , kwargs={"pk": self.pk}
