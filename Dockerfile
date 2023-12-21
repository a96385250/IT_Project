FROM python:3.7

WORKDIR /web

COPY . /web/

RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]
CMD ["uwsgi", "--ini", "uwsgi.ini"]