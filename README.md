Файл creds.json необходимо получить на сайте Google sheets https://console.cloud.google.com/apis/credentials.
В файле .env прописываем id таблицы, ID чат бота и Token бота. 
Сначала необходимо установить все зависимости с помощью команды python pip install -r requirements.txt
Для запуска проекта сначала нужно запустить сервер Django с помощью команды: python3 manage.py runserver
Затем необходимо запустить Celery с помощью команды celery -A GoogleTableScript worker -B -l INFO 
В конце запускаем frontend. Для этого переходим в директорию cd frontend 
Из директории frontend запускаем команду npm start
Можно как в принудительном порядке обновлять данные на странице, актуализировать их, так и автоматически каждые 30 секунд программа будет делать самостоятельно
Для того чтобы получать оповещения в телеграм бота, сначала нужно в @BotFatherполучить токен бота, а потом в @MyTelegramID_bot id чата. 
Ссылка на документ https://docs.google.com/spreadsheets/d/1A1tm40no_4LphRAkKfqahUH5OhVOf8YdNhuy5ilTKjQ/edit#gid=0

