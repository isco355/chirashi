FROM python:3.11-slim

RUN pip install poetry 
 
WORKDIR  backend

EXPOSE 8000
