template: inverse
# Services
---

.left-column[
    ## Services
### - Small Web
]
.right-column[
* `small-web` runs a simple HTTP server _in a container_.

```
$ docker pull sheeplepie/small-web
```

* Running it and listing ports:

```
$ docker run sheeplepie/small-web
$ sudo netstat -tulpn
...
```

* No listening port?

.info[
Ports exposed in your containers are not automatically exposed on your host.
]
]

---

.left-column[
    ## Services
### - Small Web
]
.right-column[

* Can't change port mappings on an existing container

* Need to create a new container

```
$ docker run -d -p 127.0.0.1:8000:80 sheeplepie/small-web
$ curl localhost:8000
Congrats, your container is working
```

.info[
-d, --detach : detach

-p, --publish 127.0.0.1:8000:80 : map port 80 in your container to localhost:8000
]
]

---

.left-column[
    ## Services
### - Small Web
]
.right-column[
* Inspect port mappings

```
$ docker inspect $(docker ps -ql)
...
"Ports": {
    "80/tcp": [
        {
            "HostIp": "127.0.0.1",
            "HostPort": "8000"
        }
    ]
}...
```

.info[
-l, --latest : last container
]
]

---

.left-column[
    ## Services
### - Small Web
### - Logs
]
.right-column[

* Previous container was detached

* Can still check the logs with `docker logs`:

```
$ docker logs --tail 5 -f $(docker ps -ql)
* Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
172.17.0.1 - - [18/Jan/2018 10:03:58] "GET / HTTP/1.1" 200 -
```

.info[
--tail : only show last X logs

-f, --follow : watch the logs as they come out
]
]

---


.left-column[
    ## Services
### - Small Web
### - Logs
### - Process
]
.right-column[
#### Sidetrack

* `small-web` is written in Python

* `python` process is running "in" the container.

.alert[
_but containers are not VMs_
]

* The `python` process is running directly on the host:

```
$ ps aux | grep python
user       377  0.0  0.0  10884  2260 pts/3    S+   22:22   0:00 grep --color=auto python
root     17091  0.0  0.1  93188 22080 ?        Ss   20:38   0:01 python3 /app/app.py
```
]

---

.left-column[
    ## Services
### - Small Web
### - Logs
### - Process
### - Exec
]
.right-column[

* Exec commands on a running container with `docker exec`:

```
$ docker exec -it $(docker ps -ql) echo hello world
hello world
```
]

---

.left-column[
    ## Services
### - Small Web
### - Logs
### - Process
### - Exec
### - Gotcha
]
.right-column[

.info[
**Caution** Containers can talk to eachother even if their services are not exposed on the host.
]

```
$ docker run -d sheeplepie/small-web
$ docker run -it alpine /bin/sh
/ # apk update; apk add curl
/ # curl 172.17.0.2
Congrats, your container is working
```
]

---

.left-column[
    ## Services
### - Small Web
### - Logs
### - Process
### - Exec
### - Gotcha
]
.right-column[
**TL;DR**

.center[
By default containers are all connected to the Docker "bridge" network and can talk to each other.
]

* You can change this with the `--network` flag
]

---

.left-column[
    ## Services
### - Small Web
### - Logs
### - Process
### - Exec
### - Gotcha
### - Exercises
]
.right-column[
.center[
**Exercises**
]
]
