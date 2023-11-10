from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from ..models import Note
from ..serializer import NoteSerializer
from ..permission import IsOwnerOrReadOnly
from config import createNote, readNote, updateNote, deleteNote


class NoteView(APIView):
    """Note using the note <id>"""

    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_object(self, id):
        obj = get_object_or_404(Note, pk=id)
        self.check_object_permissions(self.request, obj)
        return obj
    
    def get(self, request, id):
        note = self.get_object(id)
        serializer = NoteSerializer(note, many=False)
        readNote(request.user.username, note.title)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        note = self.get_object(id)
        temp = note.title
        serializer = NoteSerializer(note, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            titles = {'former': temp, 'new': serializer.validated_data['title']}
            updateNote(request.user.username, titles)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        note = self.get_object(id)
        note.delete()
        deleteNote(request.user.username, note.title)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateNote(APIView):
    """Create a note for a user"""
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = NoteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            createNote(request.user.username, serializer.validated_data['title'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)