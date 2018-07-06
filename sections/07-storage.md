template: inverse
# Storage

---

.left-column[
    ## Storage
### - Mounting
]
.right-column[
* Containers are closed file-systems

* In a stopped container, data persists

* but not in an easily accessible way from outside the container
]

---

.left-column[
    ## Storage
### - Mounting
]
.right-column[
* Can mount directories in containers:

```
$ mkdir /tmp/database
$ docker run -v /tmp/database:/data/db -d -p 127.0.0.1:27017:27017 mongo
```

.info[
-v, --volume : host/path:container/path
]
]

---

.left-column[
    ## Storage
### - Mounting
### - Named Volumes
]
.right-column[
* _Named volumes_ work like volumes

* Instead of specifying a path on the host, just use a _name_

```
$ docker run -v my-named-volume:/data/db -d -p 127.0.0.1:27017:27017 mongo
$ docker volume ls
local               my-named-volume
$ docker volume inspect my-named-volume 
[
    {
        "CreatedAt": "2018-01-19T10:25:53Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/my-named-volume/_data",
        "Name": "my-named-volume",
        "Options": {},
        "Scope": "local"
    }
]
```
]

---

.left-column[
    ## Storage
### - Mounting
### - Named Volumes
### - Copying
]
.right-column[
* If you forgot volume or want to copy an arbitrary file:

```
$ docker cp $(docker ps -ql):/data/db /tmp/db
```

.info[
container_id:/from/container/path /to/host/path
]

.info[
works in both directions, like `scp`
]
]

---

.left-column[
    ## Storage
### - Mounting
### - Named Volumes
### - Copying
### - Pro-tip
]
.right-column[
**Pro-tip**
Browse a running container by going to `/proc/pid/root/`:

```
$ sudo bash
# cd /proc/$(docker inspect --format {{.State.Pid}} `docker ps -ql`)/root
# pwd
/proc/13874/root/
```
]

---

.left-column[
    ## Storage
### - Mounting
### - Named Volumes
### - Copying
### - Pro-tip
### - Exercises
]
.right-column[

.center[
**Exercises**
]
]
