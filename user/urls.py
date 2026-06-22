from rest_framework.urls import path


from user.views import (
    ListUserView,
    UserByUsernameView,
    UserByEmailView,
    LoginView,
    RegisterView,
    UpdateUserView,
    DeleteUserView,
    RecoverUserView,
    SendEmailPasswordResetView,
    SendEmailReactivationUserView
)


urlpatterns = [
    path(
        'user/list/',
        ListUserView.as_view(),
        name='User list'
    ),
    path(
    'username/<str:username>',
    UserByUsernameView.as_view(),
    name='User-Username'
    ),
    path(
        'email/<str:email>',
        UserByEmailView.as_view(),
        name='User-email'
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),
    path(
        'update/<int:id>',
        UpdateUserView.as_view(),
        name='update-user'
    ),
    path(
        'delete/<int:id>',
        DeleteUserView.as_view(),
        name='delete-user'
    ),
    path(
        'recover/<str:email>',
        RecoverUserView.as_view(),
        name='recover-user-by-email'
    ),
    path(
        'email/reset/password/<str:username>/<str:email>/',
        SendEmailPasswordResetView.as_view(),
        name='send-recover-email'
    ),
    path(
        'email/reactivation/user/<str:username>/<str:email>/',
        SendEmailReactivationUserView.as_view(),
        name='send-reactivation-email'
    )
]
