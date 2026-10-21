from rest_framework import serializers
from Repository.models import QuestionsDB


class QuestionsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    language = serializers.ChoiceField(choices=QuestionsDB.LANGUAGE_CHOICES)
    difficulty_level = serializers.ChoiceField(choices=QuestionsDB.DIFFICULTY_CHOICES, default='easy')
    topic = serializers.CharField(max_length=100)
    notes = serializers.CharField()
    published_date = serializers.DateTimeField(read_only=True)
    sample_input = serializers.CharField()
    sample_output = serializers.CharField()
    is_active = serializers.BooleanField(default=True)

class SubmissionSerializer(serializers.Serializer):
    question_id=serializers.IntegerField()
    answer=serializers.CharField()
    points=serializers.IntegerField(read_only=True)    
    owner=serializers.CharField()
    remarks=serializers.CharField(read_only=True)
    submission_date=serializers.DateTimeField(read_only=True)

    def validate(self, validate_data):
        question_id= validate_data.get("question_id")
        if not QuestionsDB.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question does not exist....")
        return validate_data