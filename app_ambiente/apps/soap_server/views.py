# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def auth_user(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	data_json = {}
	user = authenticate(username = username, password = password)
	if user is None:
		data_json['error'] = 'Usuario o/y contraseña incorrecta'
	else:
		data_json['key_user'] = user.profileuser.key_user
	response = HttpResponse(json.dumps(data_json), content_type = 'application/json')
	response["Access-Control-Allow-Origin"] = "*"
	response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
	response["Access-Control-Allow-Headers"] = "X-Requested-With"
	return response