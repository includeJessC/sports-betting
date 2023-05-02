FROM python:3.7

RUN mkdir -p /usr/src/auth
WORKDIR /usr/src/auth

COPY requirements.txt /usr/src/auth/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/auth

EXPOSE 80

ENTRYPOINT ["python3"]

CMD ["-u", "author.py"]