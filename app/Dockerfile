FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP /usr/src/app

WORKDIR $APP

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libffi-dev jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev \
            tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev

RUN pip install --upgrade pip

COPY requirements.txt $APP/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh $APP/entrypoint.sh

COPY . $APP/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
