from django.conf.urls import url
from . import views

app_name = 'stuff'
urlpatterns = [
url(r'^discount_codes/$', views.discount_codes, name='discount_code'),

]
