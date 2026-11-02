from django.contrib import admin
from django.urls import path,include
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.course_list,name='course_list'),
    path('course/<int:course_id>/',views.course_detail,name='course_detail'),
    path('login/', views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('enroll/<int:course_id>/',views.enroll_course,name='enroll_course'), 
    path('my-courses/',views.my_courses,name='my_courses'),   
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )