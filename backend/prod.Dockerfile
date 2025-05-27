FROM python:3.11-slim

RUN pip install poetry 
 
WORKDIR  backend

RUN cd /backend

copy . .

RUN poetry install  --no-root

EXPOSE 8000


# CMD ["poetry", "run", "python3", "main.py" ]

