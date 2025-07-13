from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# def index(request):
#     return HttpResponse("Eat No Meat for the entire Month")


# def February(request):
#     return HttpResponse("Walk for 20kms Everyday")


monthly_challenges={
    "January": "Eat No meat for 30 days",
    "February" : "Walk for atleast 20 Mins Everyday",
    "March": "Learn Django for 20mins everyday",
    "April": "Eat No meat for 30 days",
    "May": "Walk for atleast 20 Mins Everyday",
    "June": "Eat No meat for 30 days",
    "July": "Learn Django for 20mins everyday",
    "December": None
    
}

def index(request):
    months= list(monthly_challenges.keys())
    return render(request,"Challenges/index.html",{
        "months": months
        
    })
    
    
    
    
    
    # res_list=""
    # for month in months:
    #     month_path= reverse("challenge-main",args=[month])
    #     capitalized_month=month.capitalize()
    #     res_list+=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # respose_data=f"<ul>{res_list}</ul>"
    # return HttpResponse(respose_data)


def monthy_challenges_by_number(request,month):
    months=list(monthly_challenges.keys())
    if month> len(months):
        return HttpResponseNotFound("wtf are you typing boi")
    month_redirected= months[month-1]
    redirected_path=reverse("challenge-main",args=[month_redirected])
    return HttpResponseRedirect(redirected_path)





def monthy_challenges(request,month):
   
    challenge_var=monthly_challenges[month]
    # #response_data=f"<h1>{challenge_var}</h1>"
    # response_data= render_to_string("Challenges\Challenge.html")
    # return HttpResponse(response_data)
    return render(request,"Challenges/Challenge.html",{
        "text": challenge_var,
        "month_name": month.capitalize()
    })
    # challenge_var=None
    # if month=="January":
    #     challenge_var="Do not Eat Meat for 3 Months"
    # elif month=="February":
    #     challenge_var="Walk for 20 mins Everyday"
        
    # else:
    #     challenge_var= HttpResponseNotFound
        
    # return HttpResponse(challenge_var)
           
        
    
