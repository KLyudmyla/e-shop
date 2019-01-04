At this project was realised next functionality for e-shop:
there is some registered customers and staff.
When the seller login he can see form for give discount for customer. 
Discount code is unique value that looks like A-B-C-D. 'A', 'B', 'C', 'D' can be any alphanumeric values.
When the customer login he can see the list of his discounts.

Launch of the project

`python3 -m venv myvenv`
`source myvenv/bin/activate`
`cd e_shop`
`pip install -r requirements.txt`
`python manage.py runserver`

Tests:

`python manage.py test`


Registered customer:

```
Username	Email	            Password

customer1	customer1@mail.com	qwe123qwe123
customer2	customer2@mail.com	qwe123qwe123
customer3	customer3@mail.com	qwe123qwe123
customer4	customer4@mail.com	qwe123qwe123
```

Registered staff:

```
Username	Email	            Password

staff1	    staff1@mail.com	    qwe123qwe123
staff2	    staff2@mail.com	    qwe123qwe123
```

Log in to the admin panel:

```
Username	    Password
admin	        qwe123qwe123
```
