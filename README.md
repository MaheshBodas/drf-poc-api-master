# DJango REST PoC API Server drf-poc-api-master

Source code for the [DJango REST API based on chinook schema][server].

[server]: https://github.com/MaheshBodas/chinook-poc-api-master

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


DJango REST based API based on Chinook database

  - Created chinook schema tables using reverse engineering using inspectdb command.
  - Following tables are created namely Artist, Album, MediaType, Genre, Track.
  - User can get all Track records.
  - User can filter Track records based on Album, Genre and MediaType.
  - Only authenticated users are allowed to access Track retrieval API

### For details of User guide refer following links
- [User Guide](https://github.com/MaheshBodas/chinook-poc-api-master/tree/master/blob/Chinook-PoC-WebAPI-Presentation.pdf)

### Installation

```sh
$ mkvirtualenv drf-poc-api-master
$ setprojectdir .
$ git clone https://github.com/MaheshBodas/drf-poc-api-master
$ workon drf-poc-api-master 
$ python manage.py makemigrations chinookapi
$ python manage.py migrate
S python manage.py shell
```

Creating superuser

```sh
$ manage.py createsuperuser --username=mahesh.bodas --email=mahesh.bodas@gmail.com
$ manage.py createsuperuser --username=root --email=root@example.com --noinput
```
To Run test cases
```sh 
$ python manage.py test chinookapi
```
Running application locally
```sh 
$ manage.py runserver localhost:9527
$ manage.py runserver 127.0.0.1:9527


Docker set up. Copy over all source files and build up all images within docker container.
Once docker container is up create super user

```sh
```
$ docker build .
$ docker-compose -f docker-compose.yml up -d --build
$ docker-compose exec web python manage.py createsuperuser 

