FROM python:latest
WORKDIR /usr/app/src
COPY mybot.py ./
RUN pip install --user pyTelegramBotAPI
RUN pip install --user requests
CMD ["python3", "./mybot.py"]
