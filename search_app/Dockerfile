FROM python:3.7-alpine
MAINTAINER Bauyrjan Jyenis
WORKDIR /app
COPY requirements.txt .
USER root
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
USER 1001
CMD ["python3", "search.py"]