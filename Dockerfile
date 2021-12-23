FROM python:latest
WORKDIR /usr/src/app
COPY mybot.py ./
RUN pip install --user pyTelegramBotAPI
RUN pip install --user requests
CMD ["python3", "./mybot.py"]
