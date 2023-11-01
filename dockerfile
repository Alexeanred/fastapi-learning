FROM python:3.9.18-alpine

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . .

CMD ["uvicorn", "mainapi:app", "--host", "0.0.0.0", "--port", "1000"]
