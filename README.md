****Для подключения библиотек ввести команду в командную строку:****

pip freeze > requirements.txt

****Установка пакетов:****

pip install -r requirements.txt

****Запуск сервера:****

Для запуска сервера на Windows необходимо:
- Скачать nginx
- Установить библиотеки openpyxl==3.1.5 и waitress==3.0.0
- Заменить файл nginx.conf в папке njinx/conf на файл nginx.conf из папки windows-nginx
- Прописать полные пути до файлов статики в location media, static и falicon.ico
- Запустить сервер через команду python runserver.py
- Запустить nginx, для этого зайти в cmd в папке nginx и ввести команду nginx.exe
- Перезапустить nginx можно в отдельном cmd командой nginx.exe -s reload, завершить - nginx.exe -s quit
- Заходить на сайт нужно по ссылке 127.0.0.1:8080

****Создание фикстур:****
- Создать папку с названием fixtures
- создать в ней вложенную папку с название приложения, миграции которого хотим сохранить
- Применить следующую команду:
- python manage.py dumpdata "название приложения"."название модели" > /
- fixtures/"название приложения"/"название приложения".json
- Например:
- python manage.py dumpdata tournaments.Tournaments > fixtures/tournaments/tournaments.json

****Применение фикстур:****
- применить команды makemigrations, а затем migrate
- применить команду (например): /
- python manage.py loaddata fixtures/tournaments/tournaments.json
