from playtime.models import PlayModels, Play
from playtime.serializer import PlaySerializer, MainPlaySerializer
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class PlayList(APIView):

    def get(self, request):
        play = PlayModels.objects.all()
        serializer = PlaySerializer(play, many=True)
        return Response(serializer.data)


class CreatePlay(APIView):

    def post(self, request):
        serializer = PlaySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class GetPlay(APIView):

    def get(self, request, id):
        try:
            object = PlayModels.objects.get(pk=id)
            serializer = PlaySerializer(object)
            return Response(serializer.data)

        except PlayModels.DoesNotExist:
            return Response({
                "error": "Nothing found"
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            object = PlayModels.objects.get(pk=id)
            serializer = PlaySerializer(object, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer._errors)
        except PlayModels.DoesNotExist:
            return Response({
                "error": "Nothing found"
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            object = PlayModels.objects.get(pk=id)
            object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except PlayModels.DoesNotExist:
            return Response({
                "error": "Nothing found"
            }, status=status.HTTP_404_NOT_FOUND)


class MainPlayView(APIView):

    def get(self, request):
        play = Play.objects.all()
        serializer = MainPlaySerializer(play, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MainPlaySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# @api_view(['GET'])
# def playlist(request):
#     list = PlayModels.objects.all()
#     serializer = PlaySerializer(list, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def create_play(request):

#     serializer = PlaySerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def get_play(request, id):

#     try:
#         object = PlayModels.objects.get(pk=id)

#         if request.method == 'GET':
#             serializer = PlaySerializer(object)
#             return Response(serializer.data)

#         if request.method == 'PUT':
#             object = PlayModels.objects.get(pk=id)
#             serializer = PlaySerializer(object, data=request.data)

#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer._errors)

#         if request.method == 'DELETE':
#             object = PlayModels.objects.get(pk=id)
#             object.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)

#     except PlayModels.DoesNotExist:
#         return Response({
#             "error": "Nothing found"
#         }, status=status.HTTP_404_NOT_FOUND)
