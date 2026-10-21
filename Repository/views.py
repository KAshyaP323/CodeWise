from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionsDB,SubmissionsDb
from Repository.serializers import QuestionsSerializer,SubmissionSerializer

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self, request):
        qs=QuestionsDB.objects.all()
        serializer_instance=QuestionsSerializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data=request.data
        serializer_instance=QuestionsSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionsDB.objects.create(**actual_data)
            return Response(data={"message":"Question added successfully."})
        else:
            return Response(data={"message":serializer_instance.errors})

class QuestionRetriveUpdateDeleteView(APIView):
    def get(self, request, pk):
        qs=QuestionsDB.objects.get(id=pk)        
        serializer_instance=QuestionsSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        form_data=request.data
        serializer_instance=QuestionsSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionsDB.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self, request, pk):
        QuestionsDB.objects.filter(id=pk).delete()
        return Response(data={"message":"Question deleted successfully."})    

class SubmissionListCreateView(APIView):
    def get(self, request):
            qs=SubmissionsDb.objects.all()
            submission_instance=SubmissionSerializer(qs, many=True)
            return Response(data=submission_instance.data)

    def post(self, request):
        form_data=request.data
        submission_instance=SubmissionSerializer(data=form_data)
        if submission_instance.is_valid():
            actual_data=submission_instance.validated_data
            SubmissionsDb.objects.create(**actual_data)
            return Response(data={'Message':'Answer added'})
        else:
            return Response(data=submission_instance.errors)

class SubmissionsRetriveUpdateDeleteView(APIView):
    def get(self, request, pk):
        # qs=SubmissionsDb.objects.get(id=pk)
        qs=get_object_or_404(SubmissionsDb, id=pk)
        submission_instance=SubmissionSerializer(qs)
        return Response(data=submission_instance.data)

    def put(self, request, pk):
        form_data=request.data
        submission_instance=SubmissionSerializer(data=form_data)
        if submission_instance.is_valid():
            actual_data=submission_instance.validated_data
            SubmissionsDb.objects.filter(id=pk).update(**actual_data)
            return Response(data={'Message':'Data updated'})
        else:
            return Response(data=submission_instance.errors)

class EvaluateSubmissionView(APIView):
    def put(self, request, pk):
        form_data=request.data
        SubmissionsDb.objects.filter(id=pk).update(**form_data)
        return Response(data={"Message":"Evaluated.."})
            