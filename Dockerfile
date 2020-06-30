FROM python:3
WORKDIR ~/DockerStorage/northeastern_discord_bot/
RUN pip install --no-cache-dir -r discord.py
ADD bot.py /
ADD additionalfunctions.py /
ADD userclass.py /
ADD courseclass.py /
ADD bot_key.txt /
CMD ["python", "./bot.py"]