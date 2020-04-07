# PLANEKS News

## Content

- [Installation](#installation)
    - [Preparation](#preparation)
    - [Deployment in dev environment](#deployment-in-dev-environment)
    - [Deployment in prod environment](#deployment-in-prod-environment)
- [Description](#description)
- [Admin](#admin)
- [License](#license)

## Installation

### Preparation

To deploy the application you need to install Docker and Docker compose.

For Windows and Max OS Docker Compose goes with Docker by default.

With Linux OS you need to install Docker Compose by yourself and do some post-installation steps.

- Windows:
    - https://docs.docker.com/docker-for-windows/install/


- Mac:
    - https://docs.docker.com/docker-for-mac/install/


- Linux:
    - Docker:
        - https://docs.docker.com/install/linux/docker-ce/ubuntu/
    - Post-installation steps for Linux:
        - https://docs.docker.com/install/linux/linux-postinstall/
    - Docker Compose:
        - https://docs.docker.com/compose/install/

### Deployment in dev environment

To deploy application for developing you need to run next command in your terminal (Linux and Mac) or Command Prompt
(Windows):

```shell script
docker-compose up --build
```

Or you can run docker compose in detached (background) mode. For this purpose you need to run next command:

```shell script
docker-compose up -d --build
```

To bring down docker compose containers and the associated volumes for developing you need to run next command:

```shell script
docker-compose down -v
```

Only for stopping the containers you can press Ctrl+C combination. In the next time when you need to start
docker compose after this combination you need to run next command:

```shell script
docker-compose up
```

or

```shell script
docker-compose up -d
```

With this variant of deployment your database will be flushed in every time when you start the docker compose.
When you change the code, Django server will be reload automatically, so you need not to reload it manually every time.

For superuser creating run following command and fill all needed data:

```shell script
docker-compose exec web python manage.py createsuperuser
```

Go to `http://0.0.0.0:8000/` to use site.

### Deployment in prod environment

To deploy application in production you need to run next commands in your terminal (Linux and Mac)or Command Prompt
(Windows):

```shell script
docker-compose -f docker-compose.prod.yml up --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

Or you can run docker compose in detached (background) mode. For this purpose you need to run next commands:

```shell script
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

To bring down docker compose containers and the associated volumes in production you need to run next command:

```shell script
docker-compose -f docker-compose.prod.yml down -v
```
Only for stopping the containers you can press Ctrl+C combination. In the next time when you need to start
docker compose after this combination you need to run next command:

```shell script
docker-compose -f docker-compose.prod.yml up
```

or

```shell script
docker-compose -f docker-compose.prod.yml up -d
```

For superuser creating run following command and fill all needed data:

```shell script
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

Go to `http://0.0.0.0:1337/` to use site.

## Description

PLANEKS News - implementation of a simple news site using Python and Django Framework on the backend side.

For creating the news posts is used Markdown language. The user can also attach a photos to post in the same edit form.
Also any authorized user can create post, can edit self posts and can comment any post.
In case of commenting, the creator of the post receives a notification by mail.

For sending of emails is used SendGrid SMTP service. Sending mail passes asynchronously through RabbitMQ message broker
and Celery worker.

By default, there are three groups of users:
- user (with pre moderation permission), this is default group after registration
- editor (without pre moderation permission)
- administrator (without pre moderation permission)

But administrator can change this permission for any group of users through admin site.

Editors also have access to admin site when administrator will make them staff.

Moving a post to published and back is done directly through the admin panel. The administrator or editor needs to set
the appropriate value in the `status` field of the post.

## Admin

Link for admin site: `http://0.0.0.0:8000/planeks_news_admin/`

## License

Collision is an open-sourced software licensed under the [MIT license](LICENSE.md).
