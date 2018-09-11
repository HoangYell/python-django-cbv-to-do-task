from django.conf.urls import url
from app_one import views


app_name = 'app_one'

urlpatterns = [
    url(r"^$", views.TaskList.as_view(), name="task_list"),
    url(r"^task/new/$", views.CreateTask.as_view(), name="create_task"),
    url(r"^task/update/(?P<pk>\d+)/$",
        views.UpdateTask.as_view(), name="update_task"),
    url(r"^task/delete/(?P<pk>\d+)/$",
        views.DeleteTask.as_view(), name="delete_task"),
]
