FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /api

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /api/entrypoint.sh
