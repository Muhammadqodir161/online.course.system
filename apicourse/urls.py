from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListCreateAPIView.as_view()),
    path('teachers/', views.TeacherListAPIView.as_view()),
    path('lessons/', views.LessonListCreateAPIView.as_view()),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroyAPIView.as_view()),
    path('teachers/<int:pk>/', views.TeacherRetrieveUpdateDestroyAPIView.as_view()),
    path('lessons/<int:pk>/', views.LessonRetrieveUpdateDestroyAPIView.as_view()),

]