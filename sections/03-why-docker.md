template: inverse
# Why Docker?
---

layout: false
.left-column[
    ## Why Docker?
### - Old Problems
]
.right-column[

* Companies use diff. stacks

* Teams within companies use diff. stacks

* Clients have diff. environments
]

---

layout: false
.left-column[
    ## Why Docker?
### - Old Problems
### - Legacy Deployments
]
.right-column[

* Code worked on developer's MacBook

* Broke on Linux servers

* Other users can't get it working

* Dependencies need to be re-installed

* Spin up databases and configure services

_Repeat for each ENV_
]

---

.left-column[
    ## Why Docker?
### - Old Problems
### - Legacy Deployments
### - Shipping Containers
]
.right-column[

Problems solved in other industries:

* Lingo from transport industry

* Standard container size in transport industry

* Same "box" can be loaded on ships, trains or trucks
]

---

.left-column[
    ## Why Docker?
### - Old Problems
### - Legacy Deployments
### - Shipping Containers
### - Containers for Apps
]
.right-column[
Solution: containers

* Docker containers are _portable app packages_:

    - Works on your Dev's MacBook

    - Works on your Linux servers

    - Works for your users

    - Dependencies are packaged into the containers

```
$ git clone tool
$ docker-compose up
# you're done
```
]

---

.left-column[
    ## Why Docker?
### - Old Problems
### - Legacy Deployments
### - Shipping Containers
### - Containers for Apps
### - Container TL;DR
]
.right-column[
**TL;DR**

.center[
_Containers are file systems sharing your Kernel_
]

.info[
    Windows/MacOS - Linux containers run in a Linux VM
]
]
