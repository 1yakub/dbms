from django.urls import path
from . import views
urlpatterns =[ 
    path('', views.home, name="home"),
    path('revenue',views.revenue, name="revenue"),
    path('enrollment',views.enrollment, name="enrollment"),
    path('resources',views.resources, name="resources"),
    path('data_input',views.data_input, name="data_input"),
    path('course_infos',views.course_infos, name="course_infos"),
    path('classroom_req',views.classroom_req, name="classroom_req"),

]