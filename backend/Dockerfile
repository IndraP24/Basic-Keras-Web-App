FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY api.py /app
COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]