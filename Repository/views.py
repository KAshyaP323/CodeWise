from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionsDB
from Repository.serializers import QuestionsSerializer

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