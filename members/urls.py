from django.urls import path
from .views import registrationform,editform,log_out,PasswordChangeview,Profile_page,Edit_profile_page,create_profile_page

urlpatterns=[
    path('register/',registrationform.as_view(), name='register'),
    path('edit_profile/',editform.as_view(), name='edit_profile'),
    path('create_profile/', create_profile_page.as_view(), name='create-profile'),
    path('password/',PasswordChangeview.as_view(), name='password-change'),
    path('log_out/',log_out, name='log_out'),
    path('<int:pk>/',Profile_page.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile_page/',Edit_profile_page.as_view(), name='edit_profile_page'),
]