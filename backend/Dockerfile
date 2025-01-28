###########
# BUILDER #
###########

# pull official base image
FROM python:3.11.4-slim-bookworm AS builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Set timezone
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone

# lint
RUN pip install --upgrade pip
RUN pip install flake8==6.0.0
COPY . /usr/src/app/
RUN flake8 --ignore=E501,F401,E203,E701,W503 ./backend

# install python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.11.4-slim-bookworm

LABEL maintainer="John Adams"
LABEL version="0.0.001"

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# copy logo files
#COPY ./logos/favicon.ico APP_HOME/staticfiles/favicon.ico
#COPY ./logos/logov2.png APP_HOME/staticfiles/logov2.png

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat-openbsd postgresql-client
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# copy start.sh
COPY ./start.sh .
RUN sed -i 's/\r$//g' $APP_HOME/start.sh
RUN chmod +x $APP_HOME/start.sh

# copy start.dev.sh
COPY ./start.dev.sh .
RUN sed -i 's/\r$//g' $APP_HOME/start.dev.sh
RUN chmod +x $APP_HOME/start.dev.sh

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
