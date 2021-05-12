FROM python:3.7-alpine

COPY requirenments ./

RUN pip3 install -r requirenments

COPY app.py ./app.py

HEALTHCHECK --interval=1m --timeout=5s \
  CMD curl -f http://127.0.0.1:5000/health || exit 1


EXPOSE 5000

ENTRYPOINT ["python","./app.py"]