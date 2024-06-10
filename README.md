### Работа с DRF 

##### Технологии:
- Django
- PostgreSQL
- DRF


#### Инструкция для запуска проекта:
- Клонировать проект
- Создать и активировать виртуального окружения
- Установить зависимости
- Отредактировать файл .env.sample
- Настроить БД
- Запустить проект


##### Клонирование проекта:
- git clone https://github.com/Fish8558/HW_DRF.git

##### Настройка виртуального окружение и установка зависимостей:
- [Инструкция по установке](https://sky.pro/media/kak-sozdat-virtualnoe-okruzhenie-python/)

##### Редактирование файла .env.sample
- переименовать файл .env.sample в .env и заполнить поля
    ```text
    # Postgresql
    PG_ENGINE="postgresql_psycopg2" - используем psycopg2
    PG_NAME="db_name" - название вашей БД
    PG_PGUSER="postgres" - имя пользователя БД
    PG_PASSWORD="secret" - пароль пользователя БД
    PG_HOST="host" - можно указать "localhost" или "127.0.0.1"
    PG_PORT=port - указываете порт для подключения по умолчанию 5432
    
    # Django
    SECRET_KEY=secret_key - секретный ключ django проекта
    DEBUG=True - режим DEBUG
    ```


##### Настройка БД
- примените миграции:
```text
python manage.py migrate
```
- примените фикстуры:
```text
python -Xutf8 manage.py loaddata fixtures/*.json
```

##### Запуск проекта
- запустите проект и перейдите по адресу
```text
python manage.py runserver
http://127.0.0.1:8000
```