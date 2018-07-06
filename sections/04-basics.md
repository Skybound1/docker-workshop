template: inverse
# Basics
---

.left-column[
    ## Basics
### - Images and Containers
]
.right-column[

* An **image** is an inert file system used to spin up containers

* **Containers** are live systems built from images.

| Analogies | Image | Container |
| --------- | ----- | --------- |
| Manufacturing | Blueprint | Thing |
| Programming | Class | Instance |
| Virtualization | ISO | VMs |


* one image → many containers

]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
]
.right-column[

* Searching Dockerhub for `alpine` Linux and pulling

```
$ docker search alpine
NAME                                   DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
alpine                                 A minimal Docker image based on Alpine Linux…   3024                [OK]

$ docker image pull alpine
```

.alert[
Anyone can put images on Docker Hub;
use "official repositories"
]

* Listing images

```
$ docker image ls | grep alpine
alpine                                          latest              3fd9065eaf02        9 days ago          4.15MB
```
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
]
.right-column[
* Create and run a container with our `alpine` image:

```
$ docker run alpine echo hello world
hello world
```

* Cool. Now list our containers:

```
$ docker ps -a | grep alpine
b39ab8fbb3d0        alpine                                                "echo hello world"       20 seconds ago      Exited (0) 19 seconds ago                                objective_davinci
```
.info[
-a, --all : list all
]
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
]
.right-column[
* Run it again:

```
$ docker run alpine echo hello world
hello world

$ docker ps -a | grep alpine
b39ab8fbb3d0        alpine                                                "echo hello world"       20 seconds ago      Exited (0) 19 seconds ago                                objective_davinci
2324b1d5b9d2        alpine                                                "echo hello world"       38 seconds ago      Exited (0) 37 seconds ago                                ecstatic_poitras
```

* Why do we have two containers?
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
### - Container re-use
]
.right-column[

* Containers *are* re-usable

* but they are *single function*

* Inspect container:

```
$ docker inspect f76f4a6fe596
[
    {
        "Id": "f76f4a6fe59653e88bee318493009ba87a5b77ca0cae5a13d78067be8f6eeb51",
        "Created": "2018-01-17T15:09:40.222945023Z",
        "Path": "echo",
        "Args": [
            "hello",
            "world"
        ],
...
]
```
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
### - Container re-use
]
.right-column[

* When re-used, does the same thing:

```
$ docker start -a f76f4a6fe596
hello world
```

.info[
-a, --attach : attach STDOUT/STDERR
]

To do something else, build new container
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
### - Container re-use
### - Quick Recap
]
.right-column[

.center[
    **Quick Recap**
]

* `docker search` searches for images

* `docker image pull` downloads image
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
### - Container re-use
### - Quick Recap
]
.right-column[

.center[
    **Quick Recap**
]
* `docker run` creates a new container and runs it

* `docker start` re-runs a container

* `docker ps` lists containers

* `docker inspect` shows container info
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
### - Container re-use
### - Quick Recap
]
.right-column[

.center[
    **Quick Recap**
]
.info[
**tip**
* commands that act on _images_ usually start with `docker image`

* commands that act on _containers_ usually just start with `docker`
]
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
### - Container re-use
### - Quick Recap
### - Cleaning Up
]
.right-column[
* List our images

```
$ docker image ls
alpine                                         latest              f9b6f7f7b9d3        42 hours ago        1.14MB
```

* Try to delete

```
$ docker image rm alpine
Error response from daemon: conflict: unable to remove repository reference "alpine" (must force) - container 92e35b1165e1 is using its referenced image f9b6f7f7b9d3
```
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
### - Container re-use
### - Quick Recap
### - Cleaning Up
]
.right-column[
* List containers:

```
$ docker ps -a
f76f4a6fe596        alpine                                               "echo hello world"         About an hour ago   Exited (0) About an hour ago                       tender_ramanujan
92e35b1165e1        alpine                                               "echo hello world"         About an hour ago   Exited (0) About an hour ago                       loving_tereshkova
```

.alert[
Can't delete an image referenced by containers
]

]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
### - Container re-use
### - Quick Recap
### - Cleaning Up
]
.right-column[
* Delete our containers:

```
$ docker ps -aq | xargs docker rm
f76f4a6fe596
92e35b1165e1
```

.info[
-q, --quiet : only list container IDs
]

* Now you can delete image:

```
$ docker image rm alpine
Untagged: alpine:latest
Untagged: alpine@sha256:ac2fc418f3348815e68e266a5aa1b60bc522581c96964912560a0baacc4f5c06
Deleted: sha256:f9b6f7f7b9d34113f66e16a9da3e921a580937aec98da344b852ca540aaa2242
Deleted: sha256:779f37a09c897c0406eb0a9fdc3a3eb47f973b03049d215ef7d5cede7c8f24d8
```
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
### - Container re-use
### - Quick Recap
### - Cleaning Up
### - Naming
]
.right-column[

* We used container IDs to refer to our containers

* We can give them names instead

```
$ docker run --name my-container alpine echo hello world
```

.info[
--name : container name
]

```
$ docker inspect my-container
$ docker rm my-container
```
]

---

.left-column[
    ## Basics
### - Images and Containers
### - Getting Images
### - First Container
### - Container re-use
### - Quick Recap
### - Cleaning Up
### - Naming
### - Exercises
]
.right-column[

.center[
**Exercises**

.center[
https://github.com/Skybound1/docker-workshop-exercises
]

]

]
