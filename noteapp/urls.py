from django.urls import path

from .views import CreateNote, NoteView, Notes, UserNotes

urlpatterns = [
    path('create', CreateNote.as_view(), name='create-note'),
    path('all', Notes.as_view(), name='all-notes'),
    path('<int:id>', NoteView.as_view(), name='get-a-note'),
    path('', UserNotes.as_view(), name='note'),
]