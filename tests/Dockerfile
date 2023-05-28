FROM python:3.7

RUN mkdir -p /usr/src/test
WORKDIR /usr/src/test
RUN pip3 install pytest
RUN pip3 install requests
COPY . /usr/src/test

EXPOSE 7070

ENTRYPOINT ["pytest"]

CMD ["tests.py"]