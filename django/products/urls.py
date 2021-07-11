from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name='about'),
    path('contacts',views.contacts,name='contacts'),
    path('offerindex',views.offerindex,name='offerindex')

]