# api_yatube

api для проекта 
# YATUBE "Свободное слово"
 

Площадка для размещения постов авторов,
подписок на любимых авторов
и возможностью обмена комментариев к постам.

Стек: Python, Django, Django REST Framework, Simple JWT

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/.../api_final_yatube.git
```

```
cd  api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Эндпойнты API:

```
Размещение, получение, редактирование постов
/api/v1/posts/
/api/v1/posts/{id}/
Запрос к API /api/v1/posts/
для создания поста,
запрос к API /api/v1/posts/{id}/
для редактирования, замены, удаления поста {id}.
{
  "text": "string",
  "image": "string",
  "group": 0
}

Размещение, получение, редактирование комментариев к посту
Запрос к API /api/v1/posts/{post_id}/comments/
для создания комментария, 
запрос к API /api/v1/posts/{post_id}/comments/{id}/
для редактирования, замены, удаления комментария {id}.
{
  "text": "string"
}

Получение информации о существующих группах
Создание, удаление, замена и редактирование групп через API невозможно.
/api/v1/groups/
api/v1/groups/{id}/

Управление подписками
/api/v1/follow/
Запрос к API
для создания подписки:
{
  "following": "string"
}
Редактирование, замена, удаление
существующих подписок через API невозможно.

Управление правами доступа(работа с токенами)
/api/v1/jwt/create/
/api/v1/jwt/refresh/
/api/v1/jwt/verify/

Запрос к API /api/v1/jwt/create/ 
для получения JWT-токена:
{
"username": "string",
"password": "string"
}

Запрос к API /api/v1/jwt/refresh/
для обновления JWT-токена:
{
  "refresh": "string"
}

Запрос к API /api/v1/jwt/verify/
для проверки валидности JWT-токена:
{
  "token": "string"
}
```
Для аутентификации используются JWT-токены.

У неаутентифицированных пользователей
доступ к API только на чтение.

Управление подписками могут осуществлять
только аутентифицированные пользователи.

Аутентифицированным пользователям разрешено
изменение и удаление своего контента;
в остальных случаях доступ предоставляется только для чтения.

### Мы за свободное слово!
