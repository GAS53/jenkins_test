from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

import magic

from mainapp.models.project import Project
from mainapp.models.detail import Detail
from mainapp.models.assembly import Assembly


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class BadFileView(TemplateView):
    template_name = 'mainapp/bad_file.html'

class GoodFileView(TemplateView):
    template_name = 'mainapp/good_files.html'



# def preparate_xml(file):
#     использовать здесь добавление в базу нового Project Detail и Assembly 



class NewProjectView(View):
    # template_name = 'mainapp/bad_file.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'mainapp/new_project.html')

    def post(self, request, *args, **kwargs):
        request_files_di = dict(request.FILES.items())
        if not request_files_di.get('pdf_file') or not request_files_di.get('xml_file'):
            url = reverse('mainapp:bad_file')
            return HttpResponseRedirect(url)
        
        pdf_file = request.FILES['pdf_file']
        xml_file = request.FILES['xml_file']

        # сделать ограничение на загрузку файлов по размеру

        print(pdf_file.size)  # 2990782

        print(xml_file.size) # 188

        if not 'XML' in magic.from_file(xml_file.name) or not 'PDF' in magic.from_file(pdf_file.name):
            url = reverse('mainapp:bad_file')
            return HttpResponseRedirect(url)
        
        url = reverse('mainapp:files_is_ok')
        # preparate_xml()
        # save_pdf()
        return HttpResponseRedirect(url)
        

