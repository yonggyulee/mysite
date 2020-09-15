"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views as mainviews
import guestbook.views as guestbookviews
import user.views as userviews
import board.views as boardviews

urlpatterns = [
    path('board/', boardviews.index),
    path('board/writeform', boardviews.writeform),
    path('board/write', boardviews.write),
    path('board/delete', boardviews.delete),
    path('board/view', boardviews.view),
    path('board/modifyform', boardviews.modifyform),
    path('board/modify', boardviews.modify),
    path('board/replyform', boardviews.replyform),
    path('board/reply', boardviews.reply),

    path('user/login', userviews.login),
    path('user/loginform', userviews.loginform),
    path('user/joinform', userviews.joinform),
    path('user/join', userviews.join),
    path('user/joinsuccess', userviews.joinsuccess),
    path('user/updateform', userviews.updateform),
    path('user/update', userviews.update),
    path('user/logout', userviews.logout),

    path('', mainviews.index),

    path('guestbook/', guestbookviews.index),
    path('guestbook/add', guestbookviews.add),
    path('guestbook/deleteform', guestbookviews.deleteform),
    path('guestbook/delete', guestbookviews.delete),

    path('admin/', admin.site.urls),
]
