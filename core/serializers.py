from .models import Question, Answer
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()  # the function's name must begin with get_

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, obj):  # to fetch the answers of any question
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

