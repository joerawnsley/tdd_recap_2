FROM  --platform=linux/amd64 python:3.8.2-alpine
    
RUN   mkdir  /var/flasksite

COPY  .  /var/flasksite/

WORKDIR  /var/flasksite/

RUN apk add python3 

RUN  pip3 install -r requirements.txt 

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
