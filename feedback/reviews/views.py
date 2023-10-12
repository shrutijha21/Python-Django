from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View

# Create your views here.

class ReviewView(View):
    def get(self,request):
        form= ReviewForm()
        #i am creating the form here and returning the rendered template
        return render(request,"reviews/review.html",{
        "form":form
    })

    def post(self,request):
        form=ReviewForm(request.POST)
        if form.is_valid():
             form.save()
             return HttpResponseRedirect("/thank-you")     

def thank_you(request):
    return render(request,"reviews/thankyou.html")




# def review(request):
#     if request.method == 'POST':
#         form=ReviewForm(request.POST,instance=existing_data)
#         if form.is_valid():
#           form.save()
#           return HttpResponseRedirect("/thank-you")
#         # the request has a method who's name is method which we use here and we are using if condition to check if the action is post or not
#        existing_data=Review.objects.get(pk=1)
#        form=ReviewForm(request.POST,instance=existing_data)
#        if form.is_valid():
#           form.save()
#           return HttpResponseRedirect("/thank-you")
#         #we use this return so that the url of the browser changes and we post back to a get request
#     else:
#         form= ReviewForm()


#     return render(request,"reviews/review.html",{
#          "form":form
#     })
#  #we could use the commented code above in review that is rendering thankyou.html but then it will load a html page and we dont want that
#  #so we created this than_you method which will make a new get request and open a new page rendering thank you