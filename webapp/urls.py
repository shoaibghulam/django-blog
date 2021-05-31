from django.urls import path , include
from webapp.views import *


urlpatterns = [
    path('', Index.as_view(),name="index"),
    path('posts', Posts.as_view(),name="posts"),
    path('category/<int:id>', Category.as_view(),name="category"),
    path('view/<int:id>', View.as_view(),name="view"),

    # dashboard start
    path('login',login.as_view(),name="login"),
    path('dashboard', Dashboard.as_view(),name="dashboard"),
    path('pashboardposts', DashboardPosts.as_view(),name="pashboardposts"),
   
    # path('insert', insert,name="insert"),
    path('categorydashboard', categoryDashboard.as_view(),name="categorydashboard"),
    path('categoryupdate', categoryupdate,name="categoryupdate"),
    path('categorydelete/<int:id>', categorydelete,name="categorydelete"),
    path('postupdate/<int:id>', postupdate,name="postupdate"),
    path('postdelete/<int:id>', postdelete,name="postdelete"),
    path('setting', setting,name="setting"),
    path('logout', logout,name="logout"),
    # dashboard end
]
    
   

