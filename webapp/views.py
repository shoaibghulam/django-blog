from django.shortcuts import render , HttpResponse , redirect
from django.views import View
from .models import *
from django.contrib import messages



# dashboard start 

class  login(View):
    def get(self,request):
        return render(request,'dashboard/login.html')

    def post(self,request):
        if request.method =="POST":
            try:
                email = request.POST['email']
                password = request.POST['pass']
                data=userModal.objects.get(username=email ,password=password)
                if data:
                    request.session['user']=data.pk
                    request.session['thumb']=str(data.profile.url)
                    return redirect('dashboard')
            except:
                messages.error(request,"Please Enter Correct email and Password")
                return redirect('login')
      


class Dashboard(View):
    def get(self,request):
        if not request.session.has_key('user'):
             return redirect('login')
        data={
            'data':postModal.objects.all()
        }
        return render(request,'dashboard/index.html',data)

class DashboardPosts(View):
    def get(self,request):
        if not request.session.has_key('user'):
             return redirect('login')
        data={
            'data':categoryModal.objects.all()
        }
        return render(request,'dashboard/insert.html',data)
    def post(self,request):
        if not request.session.has_key('user'):
             return redirect('login')
        if request.method =="POST":
            
            title= request.POST['title']
            cat=categoryModal.objects.get(pk=request.POST['cat'])
            Profile=request.FILES['Profile']
            desc= request.POST['desc']
            user=userModal.objects.get(pk=request.session['user'])
            data=postModal(ptitle=title,pdesc=desc,pthumbnail=Profile,category=cat,user=user)
            data.save()
            messages.success(request,"Data has been Inserted")
            return redirect('dashboard')

def postupdate(request,id):
    if not request.session.has_key('user'):
      return redirect('login')
    if request.method =="POST":

        data=postModal.objects.get(pk=id)
        data.ptitle= request.POST['title']
        data.category=categoryModal.objects.get(pk=request.POST['cat'])

        x=request.FILES.get('Profile')
        if x:
         data.pthumbnail=request.FILES.get('Profile')
        data.pdesc= request.POST['desc']
        data.user=userModal.objects.get(pk=request.session['user'])
     
        data.save()
        messages.success(request,"Data has been Updated")
        return redirect('dashboard')
    data={
        'pdata':postModal.objects.get(pk=id),
        'data':categoryModal.objects.all(),
    }

    return render(request,'dashboard/update.html',data)

def postdelete(request,id):
        if not request.session.has_key('user'):
            return redirect('login')
        data=postModal.objects.get(pk=id)
        data.delete()
        messages.error(request,"Data has been Deleted")
        return redirect('dashboard')

class categoryDashboard(View):
    def get(self, request):
        if not request.session.has_key('user'):
             return redirect('login')
       
        data={
            'data':categoryModal.objects.all()
        }
        return render(request,'dashboard/category.html',data)
    def post(self,request):
         if request.method =="POST":
            data=categoryModal(cname=request.POST['sname'])
            data.save()
            messages.success(request,"Data has been Inserted")
            return redirect('categorydashboard')

def categorydelete(request,id):
      data=categoryModal.objects.get(pk=id)
      data.delete()
      messages.success(request,"Data has been Deleted")
      return redirect('categorydashboard')

def categoryupdate(request):
    if not request.session.has_key('user'):
      return redirect('login')
    if request.method =="POST":
        data=categoryModal.objects.get(pk=request.POST['uid'])
        data.cname=cname=request.POST['sname']
        data.save()
        messages.success(request,"Data has been updated")
        return redirect('categorydashboard')
    messages.Error(request,"Not Allowed")
    return redirect('categorydashboard')


def setting(request):
    if not request.session.has_key('user'):
      return redirect('login')
    if request.method =="POST":
        data=userModal.objects.get(pk=request.session['user'])
        data.firstName = request.POST['fistname']
        data.lasetName = request.POST['lastname']
        data.email = request.POST['email']
        data.desc = request.POST['desc']
        thumb = request.FILES.get('profile')
        if thumb:
            data.profile=thumb
        data.username = request.POST['username']
        data.password = request.POST['password']
        data.save()
        request.session['thumb']=str(data.profile.url)
        messages.success(request,"User has been updated")
        return redirect("setting")
    data=userModal.objects.get(pk=request.session['user'])
    return render(request,'dashboard/setting.html',{'data':data})
    
def logout(request):
    if request.session.has_key('user'):
        del request.session['user']
        return redirect('login')
    else:
        return redirect("home")



# deashboard end
# public view start
class Index(View):
    def get(self,request):
        data={
        'about':userModal.objects.all()[0],
        'nav':categoryModal.objects.all(),
        'data':postModal.objects.all().order_by('-pk'),
    }
        return render(request,'public/index.html',data)

class Posts(View):
    def get(self,request):
        return render(request,'public/posts.html')


class Category(View):
    def get(self,request,id):
        data={
        'about':userModal.objects.all()[0],
        'nav':categoryModal.objects.all(),
        'data':postModal.objects.filter(category=id).order_by('-pk'),
        
    }
       
        return render(request,'public/category.html',data)

class View(View):
    def get(self,request,id):
        data={
        'about':userModal.objects.all()[0],
        'nav':categoryModal.objects.all(),
        'data':postModal.objects.all().order_by('-pk'),
        'single':postModal.objects.get(pk=id),
        
          }
        return render(request,'public/view.html',data)


# public view end
        