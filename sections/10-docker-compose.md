template: inverse
# Docker Compose

---

.left-column[
    ## Docker Compose
### - Purpose
]
.right-column[

* What if your containerized app needs a database?

* and a message broker?

* and another service?
]

---

.left-column[
    ## Docker Compose
### - Purpose
]
.right-column[

* You could just run several of the Docker commands we've seen so far

* That would be annoying and error prone
]

---

.left-column[
    ## Docker Compose
### - Purpose
]
.right-column[
* Meet `docker-compose`; _you already know it_

```
version: '3'

services:
    app:
        build: .
        ports:
            - 127.0.0.1:8000:80
        command: python3 /app/app.py
        depends_on: 
            - db

    db:
        image: mongo
        volumes:
            - app_data:/data/db

volumes:
    app_data:
```
]

---

.left-column[
    ## Docker Compose
### - Purpose
]
.right-column[
* Basically `docker` commands in YAML

* Write it in `docker-compose.yml`

* Run it with `docker-compose up`
]

---

.left-column[
    ## Docker Compose
### - Purpose
### - Version
]
.right-column[

* Declare the version

```
version: '3'
```
]

---

.left-column[
    ## Docker Compose
### - Purpose
### - Version
### - Services
]
.right-column[
* Containers are defined in a `services` block.

* Pre-built image:

```
    services:
        db:
            image: mongo
```

* Build your own

```
    services
        app:
            build: /dir/with/Dockerfile
```
 
* `app` and `db` will be resolvable from other containers
]

---

.left-column[
    ## Docker Compose
### - Purpose
### - Version
### - Services
]
.right-column[
* Most compose options should be obvious now:

```
    services:
        app:
            build: .
            ports:
                - 127.0.0.1:8000:80
            command: python3 /app/app.py
```
]

---

.left-column[
    ## Docker Compose
### - Purpose
### - Version
### - Services
]
.right-column[
* Other options specific to compose:

```
    services:
        app:
            ...
            depends_on: 
                - db
```

.info[
`depends_on`: `docker-compose` will spin up `db` before `app`
]
]

---

.left-column[
    ## Docker Compose
### - Purpose
### - Version
### - Services
### - Volumes
]
.right-column[
* Volumes; mount by path or by named volume:

```
    services:
        db:
            image: mongo
            volumes:
                - app_data:/data/db

    volumes:
        app_data:
```

.info[
You can't create a named volume "lazily" in `docker-compose`; you need to define it in a `volumes` block.
]


]

---

.left-column[
    ## Docker Compose
### - Purpose
### - Version
### - Services
### - Volumes
### - Exercises
]
.right-column[
.center[
**Exercises**
]
]
