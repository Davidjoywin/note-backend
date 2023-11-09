from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Note
from ..serializer import NoteSerializer


class Notes(APIView):
    """Get all notes in the db"""
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserNotes(APIView):
    """Get all notes for an authenticated user only"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        notes = Note.objects.filter(user=request.user.id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)