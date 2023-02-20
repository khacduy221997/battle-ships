from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .request import Request
from .board import Board

req = Request()
board = Board()

# Create your views here.
@api_view(['POST'])
def invite(request):
    token = request.META.get('HTTP_X_TOKEN')
    sessionId = request.META.get('HTTP_X_SESSION_ID')
    data = request.data
    req.init(sessionId, token, data)
    board.init(req.boardWidth, req.boardHeight)
    return Response({ 'success': True })

@api_view(['POST'])
def placeShips(request):
    print(req.ships)
    board.place_ships(req.ships)
    return Response()

@api_view(['POST'])
def shoot(request):
    return Response()

@api_view(['POST'])
def notify(request):
    return Response()

@api_view(['POST'])
def gameOver(request):
    return Response()
