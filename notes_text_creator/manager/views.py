from django.shortcuts import render
from django.views.generic import TemplateView

import cgi
import io
from django.http import HttpResponse
from django.views import View

def CreateText(request):
	output = io.StringIO()
	output.write("First line.\n")
	response = HttpResponse(output.getvalue(), content_type="application/octet-stream")
	response["Content-Disposition"] = "filename=text.txt"
	return response