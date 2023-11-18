from django.urls import path
from home.views import index,CategoryView,CreateSlotVeiw
urlpatterns = [
    path('',index,name="index"),
    path('creat_post/',CreateSlotVeiw.as_view(),name="creat_post"),
    path('category/<pk>',CategoryView.as_view(),name="category"),
    
]
