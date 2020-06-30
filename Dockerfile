FROM python:3
WORKDIR ~/docker_storage/northeastern_discord_bot/
RUN pip install --no-cache-dir -U discord.py
COPY bot.py /
COPY additionalfunctions.py /
COPY userclass.py /
COPY courseclass.py /
COPY bot_key.txt /
CMD ["python", "./bot.py"]