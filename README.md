Данный проект явлется моей дипломной работой.

!!!Настройки конфигурации для внедрения сайта на OSPanel/Apache находятся в конце!!!

Инструменты разработки:
1)Фреймворка Django 5.0.3 на языке программирования Python 3.12;
2)База данных на PhpMyAdmin(MySQL) и SQLite.
3)Html/CSS и JavaScript для разработки фронтенда сайта

Были разработаны функции для взаимодействуия с БД на MySQL:
1)Добавление записей в БД;
2)Удаление записей из БД;
3)Изменение сущуствующих записей и их сохранение в БД;
4)Администрация сайта;
5)Поиск/Фильтрация записей.

Настройка конфигураций OSPanel/Apache:
LoadFile "%sprogdir%/domains/Project_Django/.venv/Scripts/python312.dll"
LoadModule wsgi_module "%sprogdir%/domains/Project_Django/.venv/lib/site-packages/mod_wsgi/server/mod_wsgi.cp312-win_amd64.pyd"
WSGIPythonPath "%sprogdir%/domains/Project_Django/.venv/Lib/site-packages"

<VirtualHost *:80>
ServerAlias www.app-name.com
ServerName app-name.com
WSGIScriptAlias / "%sprogdir%/domains/Project_Django/diplom/diplom/wsgi.py"
  <Directory "%sprogdir%/domains/Project_Django/diplom/diplom">
    <Files wsgi.py>
      Require all granted
    </Files>
  </Directory>

Alias /static/ "%sprogdir%/domains/Project_Django/diplom/static/"
  <Directory "%sprogdir%/domains/Project_Django/diplom/static">
    Require all granted
  </Directory>

ErrorLog "%sprogdir%/domains/Project_Django/error.log"
CustomLog "%sprogdir%/domains/Project_Django/custom.log" common
</VirtualHost>

Шаги для установки WSGI:
https://montesariel.com/blog/post-3