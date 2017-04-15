# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^ajax/debug_ajax/$', views.debug_ajax, name='debug_ajax')
]
