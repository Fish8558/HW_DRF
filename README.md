### Работа с DRF

##### Технологии:

- Django
- PostgreSQL
- DRF
- Celery
- Redis
- Docker

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
    POSTGRES_ENGINE="postgresql_psycopg2" - используем psycopg2
    POSTGRES_DB="db_name" - название вашей БД
    POSTGRES_PGUSER="postgres" - имя пользователя БД
    POSTGRES_PASSWORD="secret" - пароль пользователя БД
    POSTGRES_HOST="host" - можно указать "localhost" или "127.0.0.1"
    POSTGRES_PORT=port - указываете порт для подключения по умолчанию 5432
    
    # Django
    SECRET_KEY=secret_key - секретный ключ django проекта
    DEBUG=True - режим DEBUG
    # Stripe API
    STRIPE_API_KEY= - секретный ключ от API Stripe
  
    # Mailing
    EMAIL_HOST_USER=test@yandex.ru - почтовый ящик Яндекса
    EMAIL_HOST_PASSWORD= - пароль ящика приложения smtp Яндекса
    
    # Redis
    REDIS=redis://host:port/0 - настройки для redis
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

>Для локального запуска проекта 

- введите команду и перейдите по адресу:

```text
python manage.py runserver
http://127.0.0.1:8000
```

- для работы с эндпоинтами используйте [Postman](https://www.postman.com/)

- для запуска worker Celery используйте команду
```text
celery -A config worker -l INFO
```
- для запуска beat Celery используйте команду
```text
celery -A config beat -l INFO -S django
```

>Для запуска контейнеров через Docker:

- установите Docker себе в систему, перейдя по [ссылке](https://docs.docker.com/engine/install/)

- для сборки проекта и запуска введите команду:
  ```text
  docker-compose up -d --build
  ```
- перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)