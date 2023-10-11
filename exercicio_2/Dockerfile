FROM python:3.11-alpine
RUN apk update && apk add poppler-utils
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["sh"]
