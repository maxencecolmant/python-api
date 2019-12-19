FROM python:slim 
#3.8.0b4-buster 

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN useradd -u 1000 --create-home -s /bin/bash appuser

RUN pip install -r requirements.txt

COPY . /app

USER 1000

EXPOSE 7070

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]