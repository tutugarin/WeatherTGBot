FROM python:latest
COPY echo_bot.py /
RUN pip install --user pyTelegramBotAPI
RUN pip install --user requests
CMD ["python3","mybot.py"]

