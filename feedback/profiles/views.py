from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    #no getpost... 1st inform abt template
    model = UserProfile#then abt model
    fields = "__all__"#about all fields
    success_url = "/profiles"#redirect url

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"



# def store_file(file):#this function helps to store the files in some or the other ways
#     with open("temp/coding.png", "wb+") as dest:#temp is the destination file
# #wb means it will write a file which is supposed to work with binary files
#         for chunk in file.chunks():#read the incoming files in chunks instead of reading it in one go.if we read a large file it will require a large memory so read in chunks
#             dest.write(chunk)




# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()#initiallized form here and use it in template
#         return render(request, "profiles/create_profile.html",{
#             "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])# we use user_image in form class and storing it into model class
#             profile.save()
#             # store_file(request.FILES["image"])
#             return HttpResponseRedirect("/profiles")
        
#         return render(request, "profiles/create_profile.html",{
#             "form": submitted_form
#         })
