from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Words
import random
from .serializer import WordsSerializer

def get_index(request):
    return render(request, "api/index.html")


@api_view(['GET'])
def get_word(request):
    words = Words.objects.all()
    serialized = WordsSerializer(words, many=True)
    return Response(random.choice(serialized.data))

@api_view(['POST'])
def post_word(request):
    serializer = WordsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_all(request):
    Words.objects.all().delete()
    return Response(status=status.HTTP_205_RESET_CONTENT)

@api_view(['GET'])
def get_n_words(request,pk):
    words = Words.objects.all()
    serialized = WordsSerializer(words, many=True)
    return Response(random.sample(serialized.data,pk))

@api_view(['GET'])
def get_definition(request,pk):
    serializer = WordsSerializer(Words.objects.filter(word__icontains=pk),many=True)
    if serializer.data != []:
        return Response(serializer.data[0],status=status.HTTP_202_ACCEPTED)
    return Response("!!Failed!!",status=status.HTTP_404_NOT_FOUND)
    

