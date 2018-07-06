template: inverse
# Building Images

---

.left-column[
    ## Building Images
### - Dockerfiles
]
.right-column[
* `Dockerfile`s define, among other things:

    - what the image contains (filesystem)

    - things the image does on build
]

---

.left-column[
    ## Building Images
### - Dockerfiles
### - Layers
]
.right-column[
* Docker images are made of layers of Dockerfiles

* `python`'s Alpine image looks like this:

```
| python3.7-rc-alpine |
| alpine              |
| scratch             |
```

* `scratch` is ... nothing

* `alpine` Dockerfile is surpisingly simple.

* `python` Dockerfile is a bit more complex.
]

---

.left-column[
    ## Building Images
### - Dockerfiles
### - Layers
### - Making a Dockerfile
]
.right-column[
* Demo: building a Dockerfile for `small-web`

```
git clone https://github.com/sheeplepie/small-web.git
```

* Create a file called Dockerfile in that directory
]

---

.left-column[
    ## Building Images
### - Dockerfiles
### - Layers
### - Making a Dockerfile
]
.right-column[
* Start from `alpine` base image

```
FROM alpine:3.6
```

* Get a copy of `app/` files in image 

```
COPY app/ /app/
```
]

---

.left-column[
    ## Building Images
### - Dockerfiles
### - Layers
### - Making a Dockerfile
]
.right-column[
* Check it out

```
$ docker image build -t my-web .
```

.info[
-t, --tag : give our image a name
]

* Run container to check files are there:

```
$ docker run -it my-web /bin/sh
/ # ls -l app/
total 8
-rw-r--r--    1 root     root           161 Jan 17 23:15 app.py
-rw-r--r--    1 root     root            14 Jan 17 22:22 requirements.txt
```
]

---

.left-column[
    ## Building Images
### - Dockerfiles
### - Layers
### - Making a Dockerfile
]
.right-column[

* Get Python and some modules:

```
RUN apk update
RUN apk add python3
RUN pip3 install -r /app/requirements.txt
```
]

---

.left-column[
    ## Building Images
### - Dockerfiles
### - Layers
### - Making a Dockerfile
]
.right-column[

* Check Python working

```
$ docker build -t my-web .
$ docker run -it my-web:latest python3
Python 3.6.1 (default, Oct  2 2017, 20:46:59) 
[GCC 6.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

]

---

.left-column[
    ## Building Images
### - Dockerfiles
### - Layers
### - Making a Dockerfile
]
.right-column[

* Give something to do when it starts:

```
CMD ["python3", "/app/app.py"]
```

]

---

.left-column[
    ## Building Images
### - Dockerfiles
### - Layers
### - Making a Dockerfile
]
.right-column[

* Party time:

```
$ docker build -t my-web .
$ docker run -d -p 8000:80 my-web
$ curl localhost:8000
Congrats, your container is working
$ docker logs $(docker ps -ql)
* Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
172.17.0.1 - - [18/Jan/2018 18:15:56] "GET / HTTP/1.1" 200 -
```
]

---

.left-column[
    ## Building Images
### - Dockerfiles
### - Layers
### - Making a Dockerfile
### - Exercises
]
.right-column[
.center[
**Exercises**
]
]
