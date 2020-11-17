from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register',views.registerpage, name='register'),
    path('login/',views.loginpage, name='login',),
    path('logout/',views.logoutuser, name='logout'),
    path('available-quizzes/', views.quizzes, name='quizzes'),
    path('quiz/<str:pk>/',views.questions, name='quiz'),
    path('save_ans/', views.save_ans, name="saveans"),
    path('result/<str:pk>/', views.results, name='result')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)