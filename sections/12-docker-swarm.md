template: inverse
# Docker Swarm

---

.left-column[
    ## Docker Swarm
### - What is it
]
.right-column[

* Group of machines (physical or virtual) that are running docker and in a cluster

* Docker commands are executed on nodes within the swarm by a swarm manager

]

---

.left-column[
    ## Docker Swarm
### - What is it
### - Why
]
.right-column[

* Desired state

* Extends docker-compose files

]


---

.left-column[
    ## Docker Swarm
### - What is it
### - Why
### - Setup
]
.right-column[
* From a node

```
docker swarm init
```

* You may need to specify an `--advertise-addr` if docker can't pick an IP

```
docker swarm init --advertise-addr <IP | Interface>
```
]

---

.left-column[
    ## Docker Swarm
### - What is it
### - Why
### - Setup
]
.right-column[
* Get a join token from a master node

```
docker swarm join-token (manager|worker)
```

* Use the given command on a new node

]

---

.left-column[
    ## Docker Swarm
### - What is it
### - Why
### - Setup
### - Deploying
]
.right-column[
```
docker stack deploy -c <COMPOSE_FILE> <STACK_NAME>
```

```
docker stack ls
```

* NOTE: Using build with docker swarm doesn't work as you think
]

---

.left-column[
    ## Docker Swarm
### - What is it
### - Why
### - Setup
### - Deploying
### - Compose file
]
.right-column[
* Your current compose files will work with minimal changes

* Can extend to tell swarm specific details about what you want (v3 and above)

```
    deploy:
        resources:
            limits:
                cpus: '0.50'
                memory: 50M
            reservations:
                cpus: '0.25'
                memory: 20M
        placement:
            constraints:
                - node.role == manager
```
]

---

.left-column[
    ## Docker Swarm
### - What is it
### - Why
### - Setup
### - Deploying
### - Compose file
]
.right-column[
* Exposed ports are exposed on _all_ nodes in the swarm

* Swarm will load balance requests to that port with all containers of that service
]

---

.left-column[
    ## Docker Swarm
### - What is it
### - Why
### - Setup
### - Deploying
### - Compose file
### - Overlay networks
]
.right-column[
* Distributed network among multiple nodes

* Allows containers on different hosts to communicate

* _OPTIONAL_ IPSec encryption (Does not work with Windows)

* Swarm management traffic is automatically encrypted
]

---

.left-column[
    ## Docker Swarm
### - What is it
### - Why
### - Setup
### - Deploying
### - Compose file
### - Overlay networks
### - Secrets
]
.right-column[
* Centrally manage secrets

* Only sent to nodes / containers that need it

* Encrypted at rest and transit

* Typically found in `/run/secrets/` within the container

```
docker secret create my_secret secret_file.txt
```
]
