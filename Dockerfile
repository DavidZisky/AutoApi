FROM python:3

RUN pip install eve

ADD app.py /
ADD settings.py /

CMD [ "python", "./app.py" ]
