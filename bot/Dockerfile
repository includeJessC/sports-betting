FROM python:3.6-alpine

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

COPY requirements.txt /usr/src/bot/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/bot

EXPOSE 9090

ENTRYPOINT ["python3"]

CMD ["bot.py"]