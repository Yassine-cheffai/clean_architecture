FROM python:3.9.6-slim-buster
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=main
ENV FLASK_ENV=development
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 5000
RUN flask db upgrade
# CMD ["flask", "--app", "main", "run", "--host=0.0.0.0"]