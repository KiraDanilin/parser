1) создадим виртуальное окружение и установим необходимые пакеты (находясь в папке проекта)

	$ sudo apt install python-virtualenv
	$ virtualenv --no-site-packages venv
	$ pip install -r requirements.txt

2) заходим в виртуальное окружение и запускаем проект при помощи gunicorn

  	$ source venv/bin/activate
	$ gunicorn -b 0.0.0.0:5000 parser_app:app --reload

3) unit-файл для автозапуска gunicorn

    [Unit]
    Description=Gunicorn instance to serve parser_app
    After=network.target
    [Service]
    User= Имя пользователя
    Group=www-data
    WorkingDirectory= Путь до проекта
    Environment="PATH=путь до проекта/venv/bin"
    ExecStart=путь до проекта/venv/bin/gunicorn --workers 3 --bind unix:parser_app.sock -b localhost:2067 -m 007 parser_app:app

4) для тестирования можно воспользоваться curl либо Postman

	$ curl -d '{"text":"тут ваш исходный текст"}' -H "Content-Type: application/json" -X POST http://localhost:2067/api/text/find_data

    Пример текста: "Дорогая Анна Петровна из гор. Москва. Просьба вернуть нам 10000 руб. сроком до 21.01.1994"