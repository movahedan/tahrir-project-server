# from datetime import datetime
import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Question, Choice
from .serializers import QuestionListPageSerializer, QuestionDetailPageSerializer, QuestionResultSerializer, ChoiceSerializer, VoteSerializer

@api_view(['GET'])
def question_result_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'GET':
        serializer = QuestionResultSerializer(question)
        return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def question_detail_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'GET':
        serializer = QuestionDetailPageSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = QuestionDetailPageSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionDetailPageSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        question.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def questions_view(request):
    if request.method == 'GET':
        # questions = []
        # for question in Question.objects.all():
        #     question_representation = {'question_text': question.question_text, 'pub_date': question.pub_date.strftime("%Y-%m-%d")}
        #     questions.append(question_representation)
        questions = Question.objects.all()
        serializer = QuestionListPageSerializer(questions, many=True)
        return Response(serializer.data)
        # return HttpResponse(json.dumps(questions), content_type='application/json')
    elif request.method == 'POST':
        serializer = QuestionListPageSerializer(data=request.data)
        if serializer.is_valid():
            # question_text = serializer.data['question_text']
            # pub_date = serializer.data['pub_date']
            # Question.objects.create(question_text=question_text, pub_date=pub_date)
            # Question.objects.create(**serializer.validated_data)
            question = serializer.save()
            return Response(QuestionListPageSerializer(question).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # question_text = request.data['question_text']
        # pub_date = datetime.strptime(request.data['pub_date'], "%Y-%m-%d")
        # return HttpResponse("Question created!", status=201)

@api_view(['POST'])
def choice_view(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            choice = serializer.save(question=question)
            return Response(ChoiceSerializer(choice).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def vote_view(request, question_id):
    if request.method == 'PATCH':
        question = get_object_or_404(Question, pk=question_id)
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            choice = get_object_or_404(Choice, pk=serializer.validated_data['choice_id'], question=question)
            choice.votes += 1
            choice.save()
            return Response("Voted")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# def question_view(request):
#     if request.method == 'GET':
#         return HttpResponce('Not Implemented')
#     elif request.method == 'POST':
#         if 'question_text' not in request.POST or 'pub_date' not in request.POST:
#             return HttpResponse("question_text or pub_date is missing", status=400)

#         question_text = request.POST['question_text']
#         pub_date = datetime.strptime(request.POST['pub_date'], '%Y-%m-%d')
#         Question.objects.create(question_text=question_text, pub_date=pub_date)
#         return HttpResponse("Question created", status=201)
