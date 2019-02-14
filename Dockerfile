FROM python:3.7.2-alpine3.9

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV PORT=8080

EXPOSE 8080

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]
