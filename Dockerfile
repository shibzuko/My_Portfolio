# Выбираем базовый образ
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Копируем файл с зависимостями в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .

# Собираем статические файлы
RUN python manage.py collectstatic --no-input --clear

# Открываем порт 8000
EXPOSE 8000

# Запускаем Gunicorn
CMD ["gunicorn", "Portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]