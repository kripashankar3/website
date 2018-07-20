from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'music'

urlpatterns = [

    url(r'^$', views.RegisterFormView.as_view(), name='register'),

    url(r'login/$', views.LoginFormView.as_view(), name='login'),

    url(r'logout/$', views.logout_view, name='logout'),

    url(r'home/$', views.album_list, name='index'),

    url(r'profile/$', views.UserView.as_view(), name='profile'),

    # music/song/
    url(r'song/$', views.song_list, name='song'),

    # music/video/
    url(r'video/$', views.video_list, name='video'),

    # music/71/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # music/album/add
    url(r'album/add/$', views.AddAlbum.as_view(), name='add-album'),

    # music/song/add
    url(r'song/add/$', views.AddSong.as_view(), name='add-song'),

    # music/video/add
    url(r'video/add/$', views.AddVideo.as_view(), name='add-video'),

    # music/album/edit/2/
    url(r'album/edit/(?P<pk>[0-9]+)/$', views.UpdateAlbum.as_view(), name='update-album'),

    # music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.DeleteAlbum.as_view(), name='delete-album'),

    # music/album_list
    url(r'album_list/$', views.AlbumList.as_view(), name='album-list'),

    # music/song_list
    url(r'song_list/$', views.SongList.as_view(), name='song-list'),

    # music/video_list
    url(r'video_list/$', views.VideoList.as_view(), name='video-list'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
