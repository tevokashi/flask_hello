FROM python:3

ENV FLASK_APP=api.py
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade -r requirements.txt
COPY app /app
COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["/usr/bin/entrypoint.sh"]
