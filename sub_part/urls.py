from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('register_form_submission',views.register_form_submission,name='register_form_submission'),
    path('login_submission',views.login_submission,name='login_submission'),
    path('back/<int:id>',views.back,name='back'),
    path('profile/<int:id>',views.profile,name="profile"),
    path('admin',views.admin,name='admin'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('admin2',views.admin2,name='admin2'),
    path('delete_id/<int:id>',views.delete_id,name='delete_id'),
    path('status_filter',views.status_filter,name='status_filter'),
    path('add_admin',views.add_admin,name='add_admin'),
    path('add_admin_data',views.add_admin_data,name="add_admin_data"),
]
