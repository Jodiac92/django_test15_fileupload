from django.shortcuts import render
from myapp.forms import DocumentForm
from myapp.models import Document
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listFunc(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        #print(form.is_valid())
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save() # upload 파일목록이 db에 저장. uploads 폴더에 파일 업로드
            #return HttpResponseRedirect('/hello')
            #print("reverse('list') : ", reverse('list'))
            return HttpResponseRedirect(reverse('list'))
        
    else:
        form = DocumentForm()
    
    documents = Document.objects.all()
    
    return render(request, 'show.html', {'form':form, 'documents':documents})
