Запуск проекта:

В командной строке вводите следующие команды:

mkdir e_shop

cd e_shop

git clone https://your_name@bitbucket.org/ximagination/judolaunch2.git

python3 -m venv myvenv

source myvenv/bin/activate

cd e_shop

pip install -r requirements.txt

http://127.0.0.1:8000 -- здесь можете смотреть проект

Запуск тестов:

python manage.py test


Зарегистрированные покупатели:

Username	Email	            Password

customer1	customer1@mail.com	qwe123qwe123

customer2	customer2@mail.com	qwe123qwe123

customer3	customer3@mail.com	qwe123qwe123

customer4	customer4@mail.com	qwe123qwe123


Зарегистрированный персонал:


Username	Email	            Password

staff1	    staff1@mail.com	    qwe123qwe123

staff2	    staff2@mail.com	    qwe123qwe123


Вход в админку:


Username	    Password

admin	        qwe123qwe123
