template: inverse
# Security

---

.left-column[
    ## Security
### - Root Shell
]
.right-column[
.alert[
Consider members of the `docker` group `root` (when daemon running)
]

* Can get a root shell if you're a member of the `docker` group

* Just mount the host's `/` in a container:

```
$ docker run -v /:/hostroot/ -it alpine /bin/sh
/ # id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)
/ # cat /hostroot/etc/shadow
root:$6$------------------------------------------------------------------------
```

* Authorisation plugins
]

---

.left-column[
    ## Security
### - Root Shell
### - Home Auto-mount
]
.right-column[
.alert[
`docker-machine` mounts your home directory in your Docker VM by default
]

* Containers can't access your stuff

* But stuff in the Docker VM could read your keys

```
$ docker-machine test
$ docker-machine ssh test
docker@test:~$ ls /hosthome/user/.ssh/
```

* Should only happen when using VirtualBox(/VMWare?) providers

* Shouldn't mount your stuff in a cloud provider

]

---

.left-column[
    ## Security
### - Root Shell
### - Home Auto-mount
### - Privileged mode
]
.right-column[
* `--privileged` flag

* All kernel capabilities

* `/dev/` device access

* Easy to breakout
]

---

.left-column[
    ## Security
### - Root Shell
### - Home Auto-mount
### - Privileged mode
### - Things to watch out for
]
.right-column[
* Mounted volumes

* UID

* Kernel capabilities

* `docker` group

* secrets

* `docker inspect` - FRIEND
]
