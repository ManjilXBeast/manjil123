from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views 

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('student/', views.student , name="student"),
    path('createstudent', views.createstudent, name="createstudent"),
    path('editstudent/<int:student_id>/', views.editstudent, name="editstudent"),
    path('readstudent/<int:student_id>/', views.readstudent, name="readstudent"),
    path('deletestudent/<int:student_id>/', views.deletestudent, name="deletestudent"),
    path('book', views.bookindex, name="bookindex"),
    path('createbook/',views.createbook, name="createbook"),
    path('editbook/<int:book_id>/',views.editbook, name="editbook"),

    # authentication system urls
    path('register', views.register, name="register"),
    path('logout', views.logout_view, name="logout"),
    path('login', auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="auth/password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordChangeDoneView.as_view(template_name="auth/password_reset_done.html"), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html"), name="password_reset_complete"),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

