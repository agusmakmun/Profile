:bust_in_silhouette: Awesome Personal Profile build on Django.

![Screenshot](https://github.com/agusmakmun/Profile/blob/master/__screenshot/profile.png)

###Technology Stack

* Python 2.7.*
* Django==1.8.7

###Demo

* https://python.web.id/agusmakmun/

###Instalation

I assume you already setup your django development with virtual enviroment (virtualenv).

**1. Create virtual enviroment and activate it.**

```
$ virtualenv your_env
$ source bin/activate
```

**2. Cloning this project**

```
$ git clone git@github.com:agusmakmun/Profile.git
```

**3. Install all requirements**

```
$ pip install -r requirements.txt
```

**4. Database migrations**

```
$ ./manage.py makemigrations
$ ./manage.py migrate
```

**5. Run the server**

```
$ ./manage.py runserver
```

###License
* [MIT](https://github.com/agusmakmun/Profile/blob/master/LICENSE)