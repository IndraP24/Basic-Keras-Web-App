FROM tiangolo/uvicorn-gunicorn:python3.8

WORKDIR /app

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]