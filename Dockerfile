FROM python:latest
COPY echo_bot.py /
RUN pip install --user pyTelegramBotAPI
CMD ["python3","mybot.py"]

