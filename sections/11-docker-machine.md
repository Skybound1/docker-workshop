template: inverse
# Docker Machine

---

.left-column[
    ## Docker Machine
### - Purpose
]
.right-column[
* `docker-machine` allows you to easily spin up docker host VMs

* Create VMs for your containers on your local hypervisor or cloud provider

* Useful if you want added isolation or set up a service on a remote host
]

---

.left-column[
    ## Docker Machine
### - Purpose
]
.right-column[
* Create a VM

```
docker-machine create hello-world
```

* Configure your Docker client to hit the remote Docker daemon:

```
eval $(docker-machine env hello-world)
```

* `docker` as normal now, just using another, remote, Docker daemon
]

---

.left-column[
    ## Docker Machine
### - Purpose
]
.right-column[
* VM has two network interfaces

    - NAT (pull images from the webz)
    
    - Host-only (you'll want to expose services that are accessible from your host)

* Check your VM IP:

```
docker-machine ip hello-world
```
]

---

.left-column[
    ## Docker Machine
### - Purpose
]
.right-column[

* Can get a shell on the VM

```
docker-machine ssh hello-world
```

* List VMs

```
docker-machine ls
```

* Start/Stop existing VM

```
docker-machine stop hello-world
docker-machine start hello-world
```
]

---

.left-column[
    ## Docker Machine
### - Purpose
]
.right-column[

* Can spawn VMs in the cloud

* The following allows you to spawn a VM in the cloud

```
docker-machine create --driver digitalocean --digitalocean-access-token=<ACCESS_TOKEN> hello-world
```

* Or with AWS

```
docker-machine create --driver amazonec2 hello-world
```

* The above will check `~/.aws/credentials` for credentials

* You can also put the access keys in as CLI arguments

]
