from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import View
from .models import Album, Song, Video
from .form import RegisterForm, LoginForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializer, SongSerializer, VideoSerializer
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404
from django.db.models import Q


class AlbumList(LoginRequiredMixin, APIView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        if not request.user.is_active or not request.user.is_active:
            raise Http404
        return Response(serializer.data)


class SongList(LoginRequiredMixin, APIView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        if not request.user.is_active or not request.user.is_active:
            raise Http404
        return Response(serializer.data)


class VideoList(LoginRequiredMixin, APIView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        if not request.user.is_active or not request.user.is_active:
            raise Http404
        return Response(serializer.data)


"""class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        if self.request.user.is_active:
            album_list = Album.objects.all()

            query = self.request.GET.get('q')
            if query:
                album_list = album_list.filter(
                    Q(album_title__icontains=query)
                ).distinct()

                paginator = Paginator(album_list, 3)  # Show 25 contacts per page
                page_request_var = 'page'
                page = self.request.GET.get(page_request_var)
                try:
                    album = paginator.page(page)
                except PageNotAnInteger:
                    album = paginator.page(1)
                except EmptyPage:
                    album = paginator.page(paginator.num_pages)

                context = {
                    'all_album': album,
                    'page_request_var': page_request_var,
                }
                return render(self.request, 'music/index.html', context)

            else:
                return Album.objects.all()"""


@login_required(function=None, redirect_field_name='redirect_to', login_url="/music/")
def album_list(request):
    if request.user.is_active:
        albums_list = Album.objects.all()

        query = request.GET.get('q')
        if query:
            albums_list = albums_list.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query) |
                Q(genre__icontains=query)
            ).distinct()

            """paginator = Paginator(albums_list, 3)  # Show 3 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        album = paginator.page(page)
    except PageNotAnInteger:
        album = paginator.page(1)
    except EmptyPage:
        album = paginator.page(paginator.num_pages)
        
        'page_request_var': page_request_var,
"""

        context = {
            'all_album': albums_list,
        }
        return render(request, 'music/index.html', context)
    else:
        raise Http404


@login_required(function=None, redirect_field_name='redirect_to', login_url="/music/")
def song_list(request):
    if request.user.is_active:
        songs_list = Song.objects.all()

        query = request.GET.get('q')
        if query:
            songs_list = songs_list.filter(
                Q(song_title__contains=query) |
                Q(album__album_title__icontains=query)
            ).distinct()

        paginator = Paginator(songs_list, 5)  # Show 3 contacts per page
        page_request_var = 'page'
        page = request.GET.get(page_request_var)
        try:
            song = paginator.page(page)
        except PageNotAnInteger:
            song = paginator.page(1)
        except EmptyPage:
            song = paginator.page(paginator.num_pages)

        context = {
            'all_song': song,
            'page_request_var': page_request_var,
        }
        return render(request, 'music/song.html', context)
    else:
        raise Http404


@login_required(function=None, redirect_field_name='redirect_to', login_url="/music/")
def video_list(request):
    if request.user.is_active:
        videos_list = Video.objects.all()

        query = request.GET.get('q')
        if query:
            videos_list = videos_list.filter(
                Q(video_title__icontains=query) |
                Q(album__artist__icontains=query)
            ).distinct()
        context = {
            'all_video': videos_list
        }
        return render(request, 'music/video.html', context)
    else:
        raise Http404


class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'
    model = Album
    template_name = 'music/detail.html'


class UserView(LoginRequiredMixin, generic.ListView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'
    model = User
    template_name = 'music/user.html'


class AddAlbum(LoginRequiredMixin, CreateView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AddSong(LoginRequiredMixin, CreateView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'
    model = Song
    fields = ['album', 'song_title', 'audio']


class AddVideo(LoginRequiredMixin, CreateView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'
    model = Video
    fields = ['album', 'video_title', 'video']


class UpdateAlbum(LoginRequiredMixin, UpdateView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class DeleteAlbum(LoginRequiredMixin, DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


"""class SongView(LoginRequiredMixin, generic.ListView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'
    template_name = 'music/song.html'
    context_object_name = 'all_song'

    def get_queryset(self):
        if self.request.user.is_active:
            songs_list = Song.objects.all()

            query = self.request.GET.get('q')
            if query:
                songs_list = songs_list.filter(
                    Q(song_title__contains=query) |
                    Q(album__album_title__icontains=query)
                ).distinct()

                paginator = Paginator(songs_list, 7)  # Show 25 contacts per page
                page_request_var = 'page'
                page = self.request.GET.get(page_request_var)
                try:
                    song = paginator.page(page)
                except PageNotAnInteger:
                    song = paginator.page(1)
                except EmptyPage:
                    song = paginator.page(paginator.num_pages)

                context = {
                    'all_song': song,
                    'page_request_var': page_request_var,
                    'title': 'List',
                }
                return render(self.request, 'music/song.html', context)
            else:
                return Song.objects.all()
        else:
            raise Http404"""


"""class VideoView(LoginRequiredMixin, generic.ListView):
    login_url = '/music/'
    redirect_field_name = 'redirect_to'
    template_name = 'music/video.html'
    context_object_name = 'all_video'

    def get_queryset(self):
        return Video.objects.all()
"""


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'music/login.html'

    # fill form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # submit
    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('music:index')

        return render(request, self.template_name, {'form': form})


class RegisterFormView(View):
    form_class = RegisterForm
    template_name = 'music/register.html'

    # fill form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # submit
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned Data(Standard format)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # return user object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return redirect('music:register')
