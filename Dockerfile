FROM python:3.9

RUN pip3 install requests

COPY . .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]