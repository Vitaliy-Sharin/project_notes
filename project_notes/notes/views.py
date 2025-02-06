from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from notes.models import Note, Folder


# Create your views here.
@require_http_methods(['GET'])
def home(request):
    user = request.user
    user_notes = []
    user_folders = []
    if user:
        user_notes = Note.objects.filter(user=user.id, parent_folder=None)
        user_folders = Folder.objects.filter(user=user.id)
    return render(request, 'home.html', {'user_notes': user_notes, 'user_folders': user_folders})


@login_required
@require_http_methods(['GET'])
def view_folder(request, id_user, id_folder):
    user = request.user
    if user.id != id_user:
        user_error = 'Данная папка принадлежит другому пользователю'
        return render(request, 'view_folder.html', {'user_error': user_error, 'folder': None, 'notes': None})
    gotten_folder = get_object_or_404(Folder, id=id_folder, user__id=id_user)
    folder_notes = Note.objects.filter(user=user.id, parent_folder__id=id_folder)
    data = {
        'user_error': None,
        'folder': gotten_folder,
        'notes': folder_notes
    }
    return render(request, 'view_folder.html', data)


@login_required
@require_http_methods(['GET'])
def view_note(request, id_user, id_note):
    user = request.user
    if user.id != id_user:
        user_error = 'Данная заметка принадлежит другому пользователю'
        return render(request, 'view_user_note.html', {'user_error': user_error})
    gotten_note = get_object_or_404(Note, id=id_note, user__id=id_user)
    data = {
        'user_error': None,
        'note': gotten_note,
    }
    return render(request, 'view_user_note.html', data)