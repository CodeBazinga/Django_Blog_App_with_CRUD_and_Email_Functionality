from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name="create"),
    path('delete/<id>/', views.deletelist,name="delete"),
    path('update/<id>', views.updatelist,name="update"),
    path('allblogs/',views.displayBlog,name="display"),
    path('email/<id>',views.sendmail,name='email'),
]


# admin username - admin
# passowrd - aptron@123