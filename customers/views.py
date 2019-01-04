from django.views.generic.detail import DetailView
from .models import Customers
from goods.models import Discount_code, Good


class CustomersDetailView(DetailView):
    model = Customers
    context_object_name = 'customer'
    template_name = 'customers/customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        customer = Customers.objects.filter(id = pk)
        discount_code = Discount_code.objects.filter(customer = customer)
        dc = []
        for code in discount_code:
            dc.append((code, Good.objects.filter(discount_code__code=code)))
        context['discount_code'] = dc
        context['users'] = Customers.objects.filter(id=pk)
        return context

class CustomersDetail_for_staffView(DetailView):
    model = Customers
    context_object_name = 'customer'
    template_name = 'customers/customer_detail_staff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        customer = Customers.objects.filter(id = pk)
        discount_code = Discount_code.objects.filter(customer = customer)
        dc = []
        for code in discount_code:
            dc.append((code, code.good, code.staff, code.date_of_issue))
        context['discount_code'] = dc
        context['users'] = Customers.objects.filter(id=pk)
        return context


