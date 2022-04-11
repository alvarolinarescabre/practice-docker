FROM python:alpine3.15

WORKDIR /usr/src/app

COPY hello.py requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "hello.py" ]
