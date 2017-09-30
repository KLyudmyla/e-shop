from django.conf.urls import url
from . import views

app_name = 'customers'
urlpatterns = [
url(r'^(?P<pk>\d+)/$', views.CustomersDetailView.as_view(), name='discount_code'),

]
