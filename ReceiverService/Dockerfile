FROM python:3.7-alpine

COPY requirenments ./

RUN pip3 install -r requirenments

COPY app.py ./app.py

EXPOSE 8080

ENTRYPOINT ["python","./app.py"]