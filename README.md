# Пульт охранника банка

Интерфейс для просмотра посещений хранилища банка сотрудниками. Показывает время входа, выхода и длительность нахождения
в хранилище.

## Установка

Склонировать репозиторий на свой компьютер. Необходим установленный Python 3.11.1

    git clone https://github.com/MilanOfc/guard_remote_control.git

Переместиться в каталог с проектом.

    cd guard_remote_control

Установить необходимые зависимости.

    pip install -r requirements.txt

## Использование

Создайте .env в корневом каталоге со следующим содержимым:

    DATABASE_HOST=YOUR_DATABASE_HOST - Which host to use when
    connecting to the database. An empty string means localhost.   
    Not used with SQLite.

    DATABASE_PORT=YOUR_DATABASE_PORT - The port to use when
    connecting to the database. An empty string means the default
    port. Not used with SQLite.

    DATABASE_NAME=YOUR_DATABASE_NAME - The name of the database to use.
    For SQLite, it’s the full path to the database file.
    When specifying the path, always use forward slashes,
    even on Windows (e.g. C:/homes/user/mysite/sqlite3.db).

    DATABASE_USERNAME=YOUR_DATABASE_USERNAME - The username to use
    when connecting to the database. Not used with SQLite.

    DATABASE_PASSWORD=YOUR_DATABASE_PASSWORD - The password to use
    when connecting to the database. Not used with SQLite.

    SECRET_KEY=YOUR_SECRET_KEY - A secret key for a particular Django installation. 
    This is used to provide cryptographic signing, 
    and should be set to a unique, unpredictable value.

    DEBUG=TRUE_OR_FALSE - A boolean that turns on/off debug mode.
    If your app raises an exception when DEBUG is True,
    Django will display a detailed traceback, including
    a lot of metadata about your environment, such as all the
    currently defined Django settings (from settings.py).

    ALLOWED_HOSTS=YOUR_ALLOWED_HOST1,YOUR_ALLOWED_HOST2... - 
    A list of strings representing the host/domain names that this
    Django site can serve. This is a security measure to prevent
    HTTP Host header attacks, which are possible even under many
    seemingly-safe web server configurations.

Запустите скрипт для локального запуска сайта:

    python manage.py runserver 0.0.0.0:8000

