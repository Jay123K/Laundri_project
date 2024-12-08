from django.urls import path
from app1 import views
from app1.views import PersonList,Customer_Update,Customer_Detail,Customer_Delete
urlpatterns = [
    path('',views.Home,name=''),
    path('Register',views.Register_page,name='Register'),
    path('Login',views.Login_page,name='Login'),
    path('Add_customer',views.Add_customer,name='Add_customer'),
    path('All_Rate',views.All_rate,name='All_Rate'),
    path('CustomerList/',PersonList.as_view(),name='CustomerList'),
    path('CustomerList/<pk>/',Customer_Detail.as_view(),name='detail'),
    path('CustomerList/<pk>/update',Customer_Update.as_view(),name='update'),
    path('CustomerList/<pk>/delete',Customer_Delete.as_view(),name='delete'),

]
