from django.shortcuts import render

from notes.models import Note, Folder


# Create your views here.
def home(request):
    user = request.user
    user_notes = []
    user_folders = []
    if user:
        user_notes = Note.objects.filter(user=user.id, parent_folder=None)
        user_folders = Folder.objects.filter(user=user.id)
    return render(request, 'home.html', {'user_notes': user_notes, 'user_folders': user_folders})

