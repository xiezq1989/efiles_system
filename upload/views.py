# -*- coding:utf8 -*-
import codecs
from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from django.contrib import messages
from django.conf import settings
from django.conf.urls.static import static
from upload.models import Upload
from upload.forms import UploadForm
from users.models import User
import pdb

# Create your views here.

def file_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.user.username
            filename=form.cleaned_data['file_url']
            file_url=form.cleaned_data['file_url']
            #pdb.set_trace()
            efile_upload=Upload()
            efile_upload.user_name=username
            efile_upload.title_name = filename
            efile_upload.file_url = file_url
            efile_upload.file_size=request.FILES['file_url'].size # Get the size of uploaded file from file's object
            efile_upload.save()
        #return HttpResponse(str(filename)+' had uploaded Success')
            messages.success(request,'上传成功')
    else:
        form = UploadForm()
    return render(request, 'upload/upload.html', {'form': form})


def search(request):
    q = request.GET.get('query')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'upload/search.html', {'error_msg': error_msg})
    post_list = Upload.objects.filter(title_name__icontains=q)
    #post_list = User.objects.filter(username__icontains=q)
    print(post_list)
    return render(request, 'upload/search.html', {#'error_msg': error_msg,
                                               'post_list': post_list})


def download(request, file_url):
   #pdb.set_trace()
   t = file_url.split("/")
   filename = t[-1]
   file_path = settings.MEDIA_ROOT + '/'+file_url
   def file_iterator(file, chunk_size=512):
      with open(file,"rb") as f:  # open file with binary mode!
         while True:
            c = f.read(chunk_size)
            if c:
               yield c
            else:
               break
   try:
      response = StreamingHttpResponse(file_iterator(file_path))
      response['Content-Type'] = 'application/octet-stream'
      response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
   except:
      return HttpResponse("Sorry but Not Found the File")
   return response


def preview(request, file_url):
    filename = file_url.split("/")[-1]
    file_type=filename.split(".")[-1]
    file_path = settings.MEDIA_ROOT + '/' + file_url
    if file_type=='pdf':
        with open(file_path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=filename.pdf'
            #pdb.set_trace()
            return response
    else:
        #mes=messages.success(request, '不是pdf文件，请下载后浏览')
        return HttpResponse('不是pdf文件，请下载后浏览')
