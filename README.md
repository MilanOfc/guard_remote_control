# Пульт охранника банка

Интерфейс для просмотра посещений хранилища банка сотрудниками. Показывает время входа, выхода и длительность нахождения
в хранилище.

## Установка

Склонировать репозиторий на свой компьтер

    git clone https://github.com/MilanOfc/guard_remote_control.git

Переместиться в каталог с проектом

    cd guard_remote_control

Установить необходимые зависимости

    pip install -r requirements.txt

## Использование

Созддайте .env в корневом каталоге со следующим содержимым:

    DATABASE_HOST=YOUR_DATABASE_HOST
    DATABASE_PORT=YOUR_DATABASE_PORT
    DATABASE_NAME=YOUR_DATABASE_NAME
    DATABASE_USERNAME=YOUR_DATABASE_USERNAME
    DATABASE_PASSWORD=YOUR_DATABASE_PASSWORD
    SECRET_KEY=YOUR_SECRET_KEY
    DEBUG=TRUE_OR_FALSE
    ALLOWED_HOSTS=YOUR_ALLOWED_HOST1,YOUR_ALLOWED_HOST2...

Запуститет скрипт для локального запуска сайта:

    python manage.py runserver 0.0.0.0:8000

