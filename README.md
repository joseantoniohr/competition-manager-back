# Competition Manager


## Project Structure


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

In order to run this project in your local environment. You should have installed docker.
If you don't have, you can get it from [here](https://www.docker.com/). 

If you have it, you are able to go to the next step.

### Installing

#### Step 1 - Build Environment

If you are in this step, you should have installed docker on your local machine. If not, you have to
go to the prerequisites section right above.

The first step is to created the build the environment in docker. For that you have to be in root 
directory an then execute this command:
```
$ docker-compose build
```

It'll take a few minutes to finish.

#### Step 2 - Run the App

This is the step to create and run the application. The command to do that is:
```
$ docker-compose up
```

#### Step 3 - Set up

We need to create database and a user that access the application, but first we have to access to the container.

```
$ docker exec -ti competition_manager bash  # Access to container

/code# python manage.py migrate  # Create database and its tables
/code# python manage.py createsuperuser  # Create to superuser to can use the application and API
```

## How to use



## Running the tests

To Run the tests in Django it's really easy. First, you should be inside the docker container, **competition_manager**.

When you are inside, you will just execute this command:

```
python manage.py test
```

If everything went ok, you will watch the next output in your terminal:

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
........
----------------------------------------------------------------------
Ran 8 tests in 3.330s

OK
Destroying test database for alias 'default'...
```

If any tests fail, the output'd be something like this:

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....E...
======================================================================
ERROR: {{ Test Function }} ({{ Test Class }})
{{ Test function description }}
----------------------------------------------------------------------
{{ Specific information about error }}
----------------------------------------------------------------------
Ran 8 tests in 3.544s

FAILED (errors=1)
Destroying test database for alias 'default'...
```

## Taking it to production



## Future improvements



## Built With

* **[Django](https://www.djangoproject.com/)** - The web framework used.
* **[Django Rest Framwork](https://www.django-rest-framework.org/)** - Toolkit for building Web APIs in Django.
* **[drf-yasg](https://github.com/axnsan12/drf-yasg)** - Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API.
* **[Django Oauth Toolkit](https://django-oauth-toolkit.readthedocs.io/en/latest/)** - Django OAuth Toolkit can help you providing 
out of the box all the endpoints, data and logic needed to add OAuth2 capabilities to your Django projects.
* **[django-allauth](https://django-oauth-toolkit.readthedocs.io/en/latest/)** - Toolkit to use a third party public OAuth provider.

## Authors

* Jose Antonio Hernández Rodríguez

## Acknowledgments

* The people who have worked with me. I've learned a lot from them. :)
* People that have created Django and Django Rest Framework. They've done a great work with this framework.
* The community, eternally grateful.
