FROM python:3.7

RUN mkdir -p /usr/src/test
WORKDIR /usr/src/test
RUN pip3 install pytest
COPY . /usr/src/test

EXPOSE 7070

ENTRYPOINT ["python3"]

CMD ["-u", "tests.py"]