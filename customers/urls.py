from django.conf.urls import url
from . import views

app_name = 'customers'
urlpatterns = [
url(r'^(?P<pk>\d+)/$', views.CustomersDetailView.as_view(), name='discount_code'),
url(r'^staff/(?P<pk>\d+)/$', views.CustomersDetail_for_staffView.as_view(), name='discount_code_staff'),

]
