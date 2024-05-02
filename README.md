# Админка с двумя кабинетами - заказчик/исполнитель
#### Стек: Python, Django, PostgreSQL

### Для работы с приложением клонируйте репозиторий:
```
git clone https://github.com/VoronovaDA/Freelance_django.git
```
### Установите виртуальное окружение и зависимости:
```
python -m venv venv
```
```
venv/Scripts/activate
```
```
pip install -r requirements.txt
```
### В файле .env запишите свои данные PostgreSQL 

### Создайте БД
```
createdb -U username dbname
```
### Создайте и проведите миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
### Создайте суперюзера для админки:
```
python manage.py createsuperuser
```
### Запустите проект:
```
python manage.py runserver
```
