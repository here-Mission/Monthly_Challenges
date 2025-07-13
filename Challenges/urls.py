from django.urls import path
from . import views


urlpatterns = [
    # path("January",views.index),
    # path("February",views.February)
    path("",views.index,name="index_no"),
    path("<int:month>",views.monthy_challenges_by_number),
    path("<str:month>",views.monthy_challenges,name="challenge-main")
   
]
