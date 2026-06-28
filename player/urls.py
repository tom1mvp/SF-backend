from rest_framework.urls import path


from player.views import (
    ListPlayerView,
    PlayerByUsernameView,
    CreatePlayerView,
    UpdatePlayerView,
    ListPlayerStatsView,
    PlayerStatsByNicknameView,
    PlayerStatsByPlayerIDView,
    CreatePlayerStatsView,
    UpdatePlayerStatsView
)

urlpatterns = [
    path(
        'list/',
        ListPlayerView.as_view(),
        name='player-list'
    ),
    path(
        'username/<str:username>',
        PlayerByUsernameView.as_view(),
        name='player-name'
    ),
    path(
        'create/',
        CreatePlayerView.as_view(),
        name='create-player'
    ),
    path(
        'update/<int:id>',
        UpdatePlayerView.as_view(),
        name='update-view'
    ),
    path(
        'stat/list/',
        ListPlayerStatsView.as_view(),
        name='plyer-stat-list'
    ),
    path(
        'stat/nickname/<str:nickname>',
        PlayerStatsByNicknameView.as_view(),
        name='player-nickname'
    ),
    path(
        'stat/id/<int:id>',
        PlayerStatsByPlayerIDView.as_view(),
        name='player-id'
    ),
    path(
        'stat/create/',
        CreatePlayerStatsView.as_view(),
        name='create-stat'
    ),
    path(
        'stat/update/<int:id>',
        UpdatePlayerStatsView.as_view(),
        name='update-player-stat-view'
    ),
]
