template: inverse
# Install Docker
---

layout: false
.left-column[
    ## Install Docker
### - Windows
]
.right-column[

You're on your own

]

---

.left-column[
    ## Install Docker
### - Windows
### - Linux
]
.right-column[
Most distros will have an antiquated version of Docker, avoid it;

Grab it fresh from Docker repos:

* https://docs.docker.com/engine/installation/#server

* (or Google: `install Docker CE $YOUR_DISTRO`)

* Then
    - `pip install docker-compose`
]

---

.left-column[
    ## Install Docker
### - Windows
### - Linux
### - docker Group
]
.right-column[
* Docker daemon binds to a Unix socket owned by `root`

* `docker` CLI needs access to that socket

* Privs++
]

---

.left-column[   
    ## Install Docker
### - Windows
### - Linux
### - docker Group
]
.right-column[
Two options:

* Prefix all commands by `sudo`

* Or add your user to the `docker` group:

```
$ sudo groupadd docker
$ sudo usermod -aG docker user
# log out and log back in
```

.alert[
Consider members of the `docker` group `root` (when daemon running)
]
]

---

.left-column[
    ## Install Docker
### - Windows
### - Linux
### - docker Group
### - Verify
]
.right-column[
Check everything works:

```
$ docker run hello-world
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```
]
