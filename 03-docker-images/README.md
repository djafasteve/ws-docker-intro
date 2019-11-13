## Docker Images :

DOcker Containers are running docker images.

Images are defined to be ran in the same way for each containers.

Multiples containers can run the same docker image, even on the same server.

#### Using an existing Image

##### DockerHub 

[Dockerhub](hub.docker.com) is the classical place were you get existing image created by the community or by the companies publishing an image of their product.


##### Pulling an Image.

Let's get a **postgresql** image.

```
sudo docker pull postgres
```
This is going to return something looking like the following.


```
Using default tag: latest
latest: Pulling from library/postgres
8d691f585fa8: Pull complete 
c991029393ff: Pull complete 
d104c69c9175: Pull complete 
0a7fb105514d: Pull complete 
c3d11c21cb77: Pull complete 
4536342c5414: Pull complete 
435bcefd4e05: Pull complete 
36b0869ae6f9: Pull complete 
5ac554d17b78: Pull complete 
61f0a5a69de4: Pull complete 
f3613132ea9e: Pull complete 
8d022c339281: Pull complete 
29616bd9cc5c: Pull complete 
6283090fa09d: Pull complete 
Digest: sha256:a4a944788084a92bcaff6180833428f17cceb610e43c828b3a42345b33a608a7
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
```

You can now see all the images you have downloaded on your computer with the following command

```
sudo docker image ls
```

You should a result looking like the following part :

```
REPOSITORY                                      TAG                 IMAGE ID            CREATED             SIZE
postgres                                        latest              f88dfa384cc4        3 weeks ago         348MB

hello-world                                     latest              fce289e99eb9        10 months ago       1.84kB

```