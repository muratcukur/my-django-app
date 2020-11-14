from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect
from .models import General_Information
from .forms import GIForm
# Create your views here.
def GeneralInformation_View(request):
    if request.method=="POST":
        form=GIForm(request.POST or None)
        if form.is_valid():
            form.save()
            GI_list=General_Information.objects.all()
            return render(request,"GeneralInformation/index.html",{"GIForm":GIForm})



    else:
        GI_list=General_Information.objects.all()
        return render(request,"GeneralInformation/index.html",{"GI_list":GI_list})
    return redirect("GeneralInformation_View")



    