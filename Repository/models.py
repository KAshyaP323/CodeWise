from django.db import models

# Create your models here.
"""
schema: QuestionsDB
Fields: title,language,notes,diificulty_level,sample_input, sample_output,
        topic, published_date, is_active.
"""
class QuestionsDB(models.Model):
    title=models.CharField(max_length=100)
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('java', 'Java'),
        ('javascript', 'JavaScript'),
    )
    language= models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='easy')
    topic=models.CharField(max_length=100)
    notes=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    sample_input=models.TextField()
    sample_output=models.TextField()
    is_active=models.BooleanField(default=True)


class SubmissionsDb(models.Model):
    question_id=models.IntegerField()
    answer=models.TextField()
    points=models.PositiveBigIntegerField(null=True)
    owner=models.CharField(max_length=100)
    submission_date=models.DateTimeField(auto_now_add=True)
    remarks=models.TextField(null=True)    