FROM python:3

RUN pip install eve
RUN mkdir -p /opt/autoapi

ADD app.py /opt/autoapi
ADD settings.py /opt/autoapi
ADD evegenie /opt/autoapi/evegenie
ADD geneve.py /opt/autoapi
ADD entrypoint.sh /

CMD [ "/entrypoint.sh" ]
