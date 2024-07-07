from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns=[
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),

    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('complete/', views.complete_reset_password, name = 'compete'),

    path('one-time-link/<uuid:token>/', views.use_one_time_link, name='use_one_time_link'),
    
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/', views.password_reset_confirm, name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
#     path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
#           name ='password_reset_confirm'),
#     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
#          name ='password_reset_complete')
]