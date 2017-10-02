from django.conf.urls import url
from . import views

app_name = 'stuff'
urlpatterns = [
url(r'^user_search/$',  views.user_search, name='user_search'),
url(r'^discount/(?P<pk>\d+)/$', views.good_search, name='discount'),
]
