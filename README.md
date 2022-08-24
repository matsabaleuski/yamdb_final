# yamdb_final
![example workflow](https://github.com/matsabaleuski/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Авторы:
- matsabaleuski
- Innis8
- Serge561

# Пример развернутого проекта

Админ Клиент:
Адрес - http://51.250.18.3/admin/
Имя пользователя - admin
Пароль - admin

Redoc:
Адрес - http://51.250.18.3/redoc/

Сервисы api:
Адреса - http://51.250.18.3/api/v1/<название_ресурса>/
Например, http://51.250.18.3/api/v1/titles/ для работы с сервисом titles
Примечание: без указания конкретного сервиса http://51.250.18.3/api/v1/ открываться не будет.


# Описание

Проект YaMDb, а также REST API сервис для него.
Приложение позволяет:
- Добавлять новые произведения в базу данных. 
- Присваивать произведениям категорию и жанры и просматривать их.
- Оставлять отзывы к произведению.
- Оставлять комментарии к отзывам.

Часть сервисов доступна только после авторизации по JWT-токену.


# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/matsabaleuski/yamdb_final.git
```

```
cd yamdb_final
```

Создать файл .env и прописать в нем переменные окружения:

```
DB_ENGINE - указать, что работаем с postgresql
DB_NAME - имя базы данных (по умолчанию postgres)
POSTGRES_USER - логин для подключения к базе данных (по умолчанию postgres)
POSTGRES_PASSWORD - пароль для подключения к БД (по умолчанию postgres)
DB_HOST - название сервиса (по умолчанию db)
DB_PORT - порт для подключения к БД (по умолчанию 5432) 
```

Запустите docker-compose из папки infra/:

```
docker-compose up
```

Выполните миграции:

```
docker-compose exec web python manage.py migrate
```

Создайте суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Соберите статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Наполнениие базы данными из файла фикстур.
Сначала скопируйте данные, например:

```
docker-compose cp ./fixtures.json web:app/fixtures.json
```

Загрузите фикстуры в БД:

```
docker-compose exec web python manage.py loaddata fixtures.json
```

Проект должен стать доступен по адресу http://localhost/

Проверьте работоспособность приложения, зайдя на http://localhost/admin/


# Как пользоваться приложением:



# Сервис AUTH

Регистрация пользователей и выдача токенов

1. Регистрация нового пользователя

Получить код подтверждения на переданный email.

Права доступа: Доступно без токена.

Использовать имя 'me' в качестве username запрещено.

Поля email и username должны быть уникальными.

Запрос:
```
 POST /api/v1/auth/signup/
```
```
{
  "email": "string",
  "username": "string"
}
```

Ответ:
```
{
  "email": "string",
  "username": "string"
}
```


2. Получение JWT-токена

Получение JWT-токена в обмен на username и confirmation code.

Права доступа: Доступно без токена.

Запрос:
```
POST /api/v1/auth/token/
```
```
{
  "username": "string",
  "confirmation_code": "string"
}
```

Ответ:
```
{
  "token": "string"
}
```


# Сервис CATEGORIES

Категории (типы) произведений

1. Получение списка всех категорий

Получить список всех категорий

Права доступа: Доступно без токена

Запрос:
```
 GET /api/v1/categories/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```


2. Добавление новой категории

Создать категорию.

Права доступа: Администратор.

Поле slug каждой категории должно быть уникальным.

Запрос:
```
POST /api/v1/categories/
```
```
{
  "name": "string",
  "slug": "string"
}
```

Ответ:
```
{
  "name": "string",
  "slug": "string"
}
```


3. Удаление категории

Удалить категорию.

Права доступа: Администратор.

Запрос:
```
 DELETE /api/v1/categories/{slug}/
```


# Сервис GENRES

Категории жанров

1. Получение списка всех жанров

Получить список всех жанров.

Права доступа: Доступно без токена

Запрос:
```
 GET /api/v1/genres/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```


2. Добавление жанра

Добавить жанр.

Права доступа: Администратор.

Поле slug каждого жанра должно быть уникальным.

Запрос:
```
POST /api/v1/genres/
```
```
{
  "name": "string",
  "slug": "string"
}
```

Ответ:
```
{
  "name": "string",
  "slug": "string"
}
```


3. Удаление жанра

Удалить жанр.

Права доступа: Администратор.

Запрос:
```
 DELETE /api/v1/genres/{slug}/
```


# Сервис TITLES

Произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

1. Получение списка всех произведений

Получить список всех объектов.

Права доступа: Доступно без токена

Запрос:
```
 GET /api/v1/titles/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]
```


2. Добавление произведения

Добавить новое произведение.

Права доступа: Администратор.

Нельзя добавлять произведения, которые еще не вышли (год выпуска не может быть больше текущего).

При добавлении нового произведения требуется указать уже существующие категорию и жанр.

Запрос:
```
 POST /api/v1/titles/
```
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Ответ:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```


3. Получение информации о произведении

Информация о произведении

Права доступа: Доступно без токена

Запрос:
```
 GET /api/v1/titles/{titles_id}/
```

Ответ:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```


4. Частичное обновление информации о произведении

Обновить информацию о произведении

Права доступа: Администратор

Запрос:
```
PATCH /api/v1/titles/{titles_id}/
```
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Ответ:
```
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```


5. Удаление произведения

Удалить произведение.

Права доступа: Администратор.

Запрос:
```
 DELETE /api/v1/titles/{titles_id}/
```



# Сервис REVIEWS

Отзывы

1. Получение списка всех отзывов

Получить список всех отзывов.

Права доступа: Доступно без токена.

Запрос:
```
 GET /api/v1/titles/{title_id}/reviews/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "score": 1,
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```


2. Добавление нового отзыва

Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение.

Права доступа: Аутентифицированные пользователи.

Запрос:
```
 POST /api/v1/titles/{title_id}/reviews/
```
```
{
  "text": "string",
  "score": 1
}
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


3. Полуение отзыва по id

Получить отзыв по id для указанного произведения.

Права доступа: Доступно без токена.

Запрос:
```
 GET /api/v1/titles/{title_id}/reviews/{review_id}/
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


4. Частичное обновление отзыва по id

Частично обновить отзыв по id.

Права доступа: Автор отзыва, модератор или администратор.

Запрос:
```
PATCH /api/v1/titles/{title_id}/reviews/{review_id}/
```
```
{
  "text": "string",
  "score": 1
}
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```


5. Удаление отзыва по id

Удалить отзыв по id

Права доступа: Автор отзыва, модератор или администратор.

Запрос:
```
 DELETE /api/v1/titles/{title_id}/reviews/{review_id}/
```


# Сервис COMMENTS

Комментарии к отзывам

1. Получение списка всех комментариев к отзыву

Получить список всех комментариев к отзыву по id

Права доступа: Доступно без токена.

Запрос:
```
 GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```


2. Добавление комментария к отзыву

Добавить новый комментарий для отзыва.

Права доступа: Аутентифицированные пользователи.

Запрос:
```
 POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
```
{
  "text": "string"
}
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```


3. Получение комментария к отзыву

Получить комментарий для отзыва по id.

Права доступа: Доступно без токена.

Запрос:
```
 GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```


4. Частичное обновление комментария к отзыву

Частично обновить комментарий к отзыву по id.

Права доступа: Автор комментария, модератор или администратор.

Запрос:
```
PATCH /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
```
{
  "text": "string"
}
```

Ответ:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```


5. Удаление комментария к отзыву

Удалить комментарий к отзыву по id.

Права доступа: Автор комментария, модератор или администратор.

Запрос:
```
 DELETE /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```



# Сервис USERS

Пользователи

1. Получение списка всех пользователей

Получить список всех пользователей.

Права доступа: Администратор

Запрос:
```
 GET /api/v1/users/
```

Ответ:
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "username": "string",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string",
        "bio": "string",
        "role": "user"
      }
    ]
  }
]
```


2. Добавление пользователя

Добавить нового пользователя.

Права доступа: Администратор

Поля email и username должны быть уникальными.

Запрос:
```
 POST /api/v1/users/
```
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

Ответ:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```


3. Получение пользователя по username

Получить пользователя по username.

Права доступа: Администратор

Запрос:
```
 GET /api/v1/users/{username}/
```

Ответ:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```


4. Изменение данных пользователя по username

Изменить данные пользователя по username.

Права доступа: Администратор.

Поля email и username должны быть уникальными.

Запрос:
```
PATCH /api/v1/users/{username}/
```
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```

Ответ:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```


5. Удаление пользователя по username

Удалить пользователя по username.

Права доступа: Администратор.

Запрос:
```
 DELETE /api/v1/users/{username}/
```
