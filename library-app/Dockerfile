FROM python:3.10.8

WORKDIR /library-app

COPY requirements.txt /library-app/requirements.txt

RUN pip install -r requirements.txt

COPY . /library-app

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

