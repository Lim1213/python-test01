# coding: utf-8
from django.shortcuts import render
from django.views.generic import TemplateView

import cgi
import io
import os
import shutil
import codecs
import urllib
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def CreateText(request):
	form = cgi.FieldStorage()
	title = request.POST.get('title')
	filePath = os.getcwd()+'/'+title
	path = os.getcwd()
	if os.path.exists(filePath):
		shutil.rmtree(filePath)
	os.makedirs(filePath)
	wf = open(os.getcwd()+'/template/01.基本情報.txt')
	data1 = wf.read()  # ファイル終端まで全て読んだデータを返す
	wf.close()
	
	data1 = data1.replace("｛案件区分｝",request.POST.get('itemDivision'))
	data1 = data1.replace("｛システム名｝",request.POST.get('systemName'))
	data1 = data1.replace("｛作業場所｝",request.POST.get('workPlace'))
	data1 = data1.replace("｛作業区分｝",request.POST.get('workDivision'))
	data1 = data1.replace("｛作業日｝",request.POST.get('workDate'))
	data1 = data1.replace("｛開始時刻｝",request.POST.get('startTime'))
	data1 = data1.replace("｛終了時刻｝",request.POST.get('endTime'))
	data1 = data1.replace("｛完了日｝",request.POST.get('compDate'))
	data1 = data1.replace("｛依頼者｝",request.POST.get('owner'))
	data1 = data1.replace("｛対応担当者｝",request.POST.get('tantou'))	
	data1 = data1.replace("｛関係者｝",request.POST.get('kankei'))
#	shutil.copy(os.getcwd()+'/template/01.基本情報.txt', title+'/')
	with codecs.open(filePath+'/01.txt','w', encoding='utf-8') as f:
		f.write(data1)
		f.close()	
		
	with codecs.open(filePath+'/02.txt','w', encoding='utf-8') as f2:
		f2.write(request.POST.get('content'))
		f2.close()
		
	if request.POST.get('genin') != "":
		with codecs.open(filePath+'/03.txt','w', encoding='utf-8') as f3:
			f3.write(request.POST.get('genin'))
			f3.close()
			
	with codecs.open(filePath+'/04.txt','w', encoding='utf-8') as f4:
		f4.write(request.POST.get('taisaku'))
		f4.close()			
	shutil.make_archive(title, 'zip', root_dir= filePath)
	
	shutil.rmtree(filePath)
	
	file_path = os.path.join(settings.MEDIA_ROOT, filePath+'.zip')
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename="{fn}"'.format(fn=urllib.parse.quote(title+'.zip'))
			return response
			
	raise Http404