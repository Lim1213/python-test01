# coding: utf-8
from django.shortcuts import render
from django.views.generic import TemplateView

import cgi
import io
import os
import shutil
import codecs
from django.conf import settings
from django.http import HttpResponse
from django.views import View

def CreateText(request):
	path = os.getcwd()
	os.mkdir("test")
	wf = open(os.getcwd()+'/template/01.基本情報.txt')
	data1 = wf.read()  # ファイル終端まで全て読んだデータを返す
	wf.close()
	
	with codecs.open('test/01.基本情報.txt','w', "cp932") as f:
		f.write(data1)
		f.close()	
	
	shutil.make_archive('test', 'zip', root_dir='test')
	
	shutil.rmtree('test')
	
	file_path = os.path.join(settings.MEDIA_ROOT, 'test.zip')
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response
	raise Http404