from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound ,HttpResponseRedirect #these both are class
from django.urls import reverse
from django.template.loader import render_to_string

# def january(request):
#     return HttpResponse("This works!")#we can return anything here we are returning a string
#     #so it is just a function  that takes in a request and returns a response
# def february(request):
#     return HttpResponse("This works for february as well!")
# def march(request):
#     return HttpResponse("This works for march also")




def monthly_challenges(request, month):
    try:
        c_t=monthly_c[month]
        return render(request,"challenges/challenge.html",{#same as render to string but needs an extra arg that is request
        # response_data=render_to_string("challenges/challenge.html",{
            "text": c_t,
            "month_name": month.capitalize()
        })#f"<h1>{c_t}</h1>"#to return html
        
        #value stored in c_t will be displayed as html heading 1
        return HttpResponse(response_data)
    except:
        response=render_to_string("404.html")
        return HttpResponseNotFound(response)#<h1>No such month in the list.</h1>---previous o/p
    return HttpResponse(c_t)



#     c_t = None

#     if month == "january":
#         c_t = "This works for January!"
#     elif month == "february":
#         c_t = "This works for February as well!"
#     elif month == "march":
#         c_t = "This works for March!"
#     else:
#         return HttpResponseNotFound("No such month in the list.")

#     return HttpResponse(c_t)




def monthly_challenges_number(request,month):
    #now after i created a variable monthly_c i want this to merge with function monthly challenges so that if i enter 1 it redirects to january
    #we will start process to achieve this
    
    months= list(monthly_c.keys())#to redirect 1-january,2-february,etc
    #we are calling the keys...
    redirect_month=months[month-1]#-1 is used to get proper indexing
    redirect_path=reverse("month-challenge",args=[redirect_month])
    # we are using this to redirect
    return HttpResponseRedirect(redirect_path)#/challenges/"+redirect_month)#no need of manual redirection
    #return HttpResponse(month)





#now it is too lengthy to write if else statements in monthly_challenges function up

monthly_c={
    "january":"This works!",
    "february":"this works for february",
    "march":"this works for march",
    "april":"this works for april",
    "may":"this works for may",
    "june":"this works for june",
    "july":"this works for july",
    "august":"this works for august",
    "september":"this works for sepember",
    "october":"this works for october",
    "november":"this works for november",
    "december":None
}#after this we make certain changes in monthly_challenges function




# now i am creating a new function so that i dont have to pass everything one by one
#also when i click on the names of the keys that have been capitalized it will show the output
def index(request):
    months = list(monthly_c.keys())
    return render(request, "challenges/index.html", {
        "month_d": months  # Update the context variable name to "month_d"
    })


#below this the code was written just to get list of months names with the help of python
#    for m in months:
#        capitalized_month = m.capitalize()
#        month_path = reverse("month-challenge", args=[m])
#        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

#    # Move this line outside the loop to build the entire list
#    response_data = f"<ul>{list_items}</ul>"
   
   # Now, return the response after the loop has processed all months
   
   
   #return HttpResponse(response_data)
   
   #we can hardcode each url also like:
#    """
#     <ul>
#      <li><a href="challenges/january">January</a></li>
#     </ul>
#     """