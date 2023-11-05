# code-union

Я захостил бд на AWS RDS, и бэк на верселе. В проекте используются энв вариэйблы, я перекинул их значения Айдане, просьба вставить их в ваше окружение вручную в файле .env (файл должен находиться в самой внешней директории, на одном уровне с api и codeunion папками). В случае если бд или версель упадут просьба обратиться ко мне, я подниму, ну либо можете воспользоваться миграциями.

_**Ссылку на версель я скину так же Айдане!!!!**_

```
python manage.py migrate
```
## По таскам:

### 1. БД на авс

### 2. CRON:

Cron функция реализована, находится в api/cron.py, на данный момент раннится каждые 5 минут, можете поменять это значения в codeunion/settings.py. Я закомментил логгер и принты так как они спамят мне все, можете расскоментить чтобы проверить, либо запусить команду 

```
python manage.py runcron
```

Вы так же можете проверить работу крона запустим команду для изменения курса по айдишке (см. пункт 3). Посмотрите лист currencies после того как поменяйете значение одной из валют, а потом перепроверьте его через 5 минут, крон функция вернет все как было их XML файла

### 3. Консольная команда:

```
python manage.py python manage.py update_currency <currency_id> <value>
```
Пример использования:
```
python manage.py update_currency 1 999
```

### 4. REST API:

Использовал рест темплейты, в них к сожалению негде указывать токен, так что если хотите глянуть на сами темплейты, просьба закомментить строки 15 и 34 в файле api/views.py 

Вот эта строка:

 permission_classes = (IsAuthenticated,)

### 5. Авторизация:

Использовал jwt токены вместе с рефреш токеном, токен передаю в хедере, можете заходить с credentials который есть энв переменных (помечены как ADMIN_USER и ADMIN_PASSWORD).

либо можете отправить два curl запроса:
```
curl --location --request POST 'https://codeunion-flame.vercel.app/api/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "ADMIN_USER",
    "password": "ADMIN_PASSWORD"
}'
```

тут вы должны получить акцесс токен и рефреш токен, далее берете акцесс токен и:
```
curl --location --request GET 'https://codeunion-flame.vercel.app/api/currencies/' \
--header 'Authorization: Bearer <access_token>'
```

### 6. Тесты:

Сделал 4 теста, два теста на эндпоинты без предоставления акцесс токена, если все верно должен возвращаться ответ 401, и два теста на эндпоинты с предоставлением акцесс токена. Запускать тесты командоы
```
python manage.py test
```

#

В случае если захотите развернуть все у себя, для начала установите все необходимые библиотеки командой
```
pip install -r requirements.txt
```

Если будет выходить ошибка с pcycopg2, то замените psycopg-binary на просто psycopg в requirements.txt
Далее просто запускаете сервер
```
python manage.py runserver
```
