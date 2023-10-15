from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView#specifically allows you to build a class that render templates
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review
# Create your views here.

class ReviewView(CreateView):
    model=Review
    form_class= ReviewForm
    template_name="reviews/review.html" #it is replacing the code below:
    success_url="thank-you"


# class ReviewView(FormView):#this class was basically made to handle get and post requests
# #we can replace all the get post method by formview
#     form_class=ReviewForm 
#     template_name="reviews/review.html" #it is replacing the code below:
#     # def get(self,request):
#     #     form= ReviewForm()
#     #     #i am creating the form here and returning the rendered template
#     #     return render(request,"reviews/review.html",{
#     #     "form":form
#     # })
   
#     success_url="thank-you"#redirects to thank you page but doesnt save the , it will not take it as post request if no redirection page is given it will give error even though the data provided s correct
#     #to save te data and see it in revews url:

#     def form_valid(self,form):
#         form.save()
#         return super().form_valid(form)#check form is having all valid data and save it
#     # def post(self,request):
#     #     form=ReviewForm(request.POST)
#     #     if form.is_valid():
#     #          form.save()
#     #          return HttpResponseRedirect("/thank-you")   





class ThankYouView(TemplateView):#with this no need to define a get method and return anything ..
    #django will automatically take a get request and return the template if the get request reaches this view
    #this type of view is associated with some specific url and when there is a get request by the user in that url django calls this view method
    template_name="reviews/thankyou.html"
    
    def get_context_data(self, **kwargs):
        #get_context_data:a func inherited by templateview.
        #main func:  to prepare context data which is then called in template(html file it is pointing to).        context= super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context["message"]="This Method Works!!!"
        return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model=Review #pointing at model class as we are now not using templat view here
    context_object_name="reviews"#have to use this context_object_name because if i will not use it here i have to use object_list instead of reviews in for loop in review_list.html

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"]= reviews
    #     return context




class SingleReviewView(DetailView):
     template_name = "reviews/single_review.html"
     model=Review#i have to chsnge the name in urls.py .. and in place of id i have to keep it pk==primary key

    #  def get_context_data(self, **kwargs):#kwargs is stored from the url... that is int:id -- part
    #     context = super().get_context_data(**kwargs)
    #     review_id= kwargs["id"]#if u use any other name than id in url then use it here also
    #     selected_review= Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context












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







    #def get(self,request):
        
    #     return render(request,"reviews/thankyou.html")
    
# def thank_you(request):
#     return render(request,"reviews/thankyou.html")
