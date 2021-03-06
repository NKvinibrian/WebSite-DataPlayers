from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from core.models import Player

import json


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Index")

    @csrf_exempt
    def post(self, *args, **kwargs):
        try:
            body = self.request.body.decode('utf-8')
            #body.replace(":", "")
            content = json.loads(body)
            if not Player.objects.filter(Nome=content['Nome']).exists():
                Player.objects.create(Nome=content['Nome'], Xp=content['Xp'], PosX=content['Pos']['X'], PosY=content['Pos']['Y'], PosZ=content['Pos']['Z'], Helmet=content['Armor']['Helmet'], Chestplate=content['Armor']['Chestplate'], Leggings=content['Armor']['Leggings'], Boot=content['Armor']['Boots'])
            print(content)
            return HttpResponse("recebido")
        except:
            return HttpResponse("Algo deu de errado")
