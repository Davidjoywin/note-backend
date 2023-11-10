from rest_framework.serializers import ModelSerializer

from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

    def validate(self, data):
        return data
    
    def create(self, validated_data):
        # user = self.context['request'].user
        # note = Note.objects.create(user=user, **validated_data)
        note = Note.objects.create(**validated_data)
        note.save()
        return note