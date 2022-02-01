FROM python:3.7-alpine
MAINTAINER Bauyrjan Jyenis
WORKDIR /app
COPY requirements.txt .
USER root
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
USER 1001
HEALTHCHECK --interval=2s --retries=5 CMD curl --fail http://localhost || exit 1
CMD ["python3", "jobs.py"]