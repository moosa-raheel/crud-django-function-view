from django.urls import path
from enroll import views

urlpatterns = [
    path("",views.show_add,name="home"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("update/<int:id>",views.update,name="update"),
]