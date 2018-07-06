template: inverse
# Checking Inside

---

.left-column[
    ## Checking Inside
### - Host System
]
.right-column[
* Check out our _host_ distribution:

```
$ cat /etc/lsb-release 
LSB_VERSION=1.4
DISTRIB_ID=Arch
DISTRIB_RELEASE=rolling
DISTRIB_DESCRIPTION="Arch Linux"
```

* and _host_ kernel:

```
$ uname -ar
Linux system0 4.14.12-1-ARCH #1 SMP PREEMPT Fri Jan 5 18:19:34 UTC 2018 x86_64 GNU/Linux
```
]

---

.left-column[
    ## Checking Inside
### - Host System
### - Container System
]
.right-column[
* Same for a Ubuntu container:

```
$ docker search ubuntu
$ docker pull ubuntu
```

* Create container and get shell in it:

```
$ docker run -it ubuntu /bin/bash
root@e650364a5a65:/# 
```

.info[
-i, --interactive : redirect STDIN

-t, --tty : pseudo-terminal
]
]

---

.left-column[
    ## Checking Inside
### - Host System
### - Container System
]
.right-column[
* _Container_ distribution:

```
root@53d9dbca684a:/# cat /etc/lsb-release 
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.3 LTS"
```

* "_Container_ kernel":

```
root@53d9dbca684a:/# uname -ar
Linux 53d9dbca684a 4.14.12-1-ARCH #1 SMP PREEMPT Fri Jan 5 18:19:34 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

.info[
Container is running a **Ubuntu file system**

has **Ubuntu binaries** and the **Ubuntu repos**

**_but is using the host's kernel_**
]
]

---

.left-column[
    ## Checking Inside
### - Host System
### - Container System
### - Gotcha
]
.right-column[
* Ubuntu usually ships with `python`, but:

```
root@53d9dbca684a:/# python
bash: python: command not found
```

* Docker images are minimalist

* Shipped with the bare essentials:

```
root@53d9dbca684a:/# dpkg -l | wc -l
101
```
]

---

.left-column[
    ## Checking Inside
### - Host System
### - Container System
### - Gotcha
### - Exercises
]
.right-column[

.center[
**Exercises**
]

]
