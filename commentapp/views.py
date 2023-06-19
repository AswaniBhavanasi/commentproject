from django.shortcuts import render,redirect

from.models import commentdata
def comment (request):
    if request.method=='GET':
        data= commentdata.objects.all().order_by('-id')
        return render(request,'comment.html',{'abcd':data})
    else:
        commentdata(
            comment= request.POST['name']
        ).save()
        return redirect(comment)
