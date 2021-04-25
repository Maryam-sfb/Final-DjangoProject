from rest_framework.views import APIView
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Answer
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer_data = QuestionSerializer(instance=questions, many=True).data
        return Response(serializer_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = QuestionSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)   # to identify has_object_permission function
        serializer_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_200_OK)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)  # by default pk is id. but we can change it to any field
        self.check_object_permissions(request, question)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









