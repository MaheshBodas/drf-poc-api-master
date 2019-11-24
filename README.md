# DJango REST PoC API Server drf-poc-api-master

Source code for the [DJango REST PoC Server][server].

[server]: https://github.com/MaheshBodas/drf-poc-api-master

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


REST based API to for defining RiskTypes and Risk Instances based on RiskType

  - API allows users to create RiskTypes and associated RiskTypeFields
in one go with use of nested serializer.
  - During creation of Risk Instance system checks that proper referential integrity
is maintained with Risk Type.
  - While creation of Risk Fields system ensures that proper referential integrity is 
  maintained with Risk and Risk Type fields.
  - Risk API allows users to create Risk and associated RiskFields in one
go with use of nested serializer.
  - Various model validation errors in RiskType and RiskTypeFields, Risk
and RiskFields are returned to client of serve API in JSON format.

### For details of User guide refer following links
- [User Guide](https://github.com/MaheshBodas/drf-poc-api-master/tree/master/blob/DRF-PoC-WebAPI-Presentation.pdf)

### Installation

```sh
$ mkvirtualenv drf-poc-api-master
$ setprojectdir .
$ git clone https://github.com/MaheshBodas/drf-poc-api-master
$ workon drf-poc-api-master 
$ python manage.py makemigrations riskapi
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
$ python manage.py test riskapi
```
Running application locally
```sh 
$ manage.py runserver localhost:9527
$ manage.py runserver 127.0.0.1:9527
```
Run following code to deploy it to AWS (zappa_settings.json is in repository)
```sh 
$ pip install zappa
$ set AWS_ACCESS_KEY_ID={Your AWS_ACCESS_KEY_ID}
$ set AWS_SECRET_ACCESS_KEY={Your AWS_SECRET_ACCESS_KEY}
$ set AWS_DEFAULT_REGION={Your preferred region}
$ zappa deploy dev
