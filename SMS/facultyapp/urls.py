from django.urls import path,include
from . import views
app_name='facultyapp'
urlpatterns=[
    path('FacultyHomePage/',views.FacultyHomePage,name='FacultyHomePage'),
    path('Adding_task/', views.Adding_task, name='Adding_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('add_course/',views.add_course,name='add_course'),
    path('view_student_list/',views.view_student_list,name='view_student_list'),
path('logout/', views.logout, name='logout'),

]