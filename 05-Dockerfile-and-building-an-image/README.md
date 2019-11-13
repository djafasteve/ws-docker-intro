## Building our first image with a Dockerfile

Now that we know how to run an image and mount a volume we are going to build a simple Python app.

### Create the app

We will use the web framework "Flask" to quickly deploy the webapp in a container.

Please find the directory called "app" and edit the file "main.py" to output your favorite color, your favorite food and the name of your pets.
Now that we have an "app", that is fine and dandy but we need an image that can run on top of docker, right ?


### Build our own image

We are going to use a community image that was already developed for us that runs Flask properly.
Just for fun, we are going to take a look at it.
Here is the github : https://github.com/tiangolo/uwsgi-nginx-flask-docker
We will use the latest stable version, python 3.7.

There is a magic file in there called "Dockerfile" which is essentially a file created to build the image.
Because that's just what we need to run a production-grade image, we are going to re-use it.
But no need to copy-paste this, there's a super duper useful command that we can use to build our app on top of it.
But first, let's checkout where this image come from.
In this image Dockerfile, we can see that the first line is 
```
FROM tiangolo/uwsgi-nginx:python3.7
```
which definitely looks like another base image.
Let's checkout the Dockerfile of this one:
https://github.com/tiangolo/uwsgi-nginx-docker/blob/master/python3.7/Dockerfile

...Let's go all the way to the source of the image:

https://github.com/docker-library/python/blob/master/3.7/stretch/Dockerfile

.......ALL THE WAY I SAID :
https://github.com/docker-library/buildpack-deps/blob/master/stretch/Dockerfile

..............................
https://github.com/docker-library/buildpack-deps/tree/master/stretch/scm

......................................................
https://github.com/docker-library/buildpack-deps/blob/master/stretch/curl/Dockerfile

........................................................................................................
https://github.com/debuerreotype/docker-debian-artifacts/blob/fd091f0a2aa0f469ee1ff991cb99748025d567f8/stretch/Dockerfile

................................................................................................................................
https://hub.docker.com/_/scratch/

See how each layer of images is built on top of the other ?
That's the magic of Docker where you can build things really quickly on top of what already exists (but double check the licences first, building things on top of proprietary images is no fun). 


Okay, now that we know that this image is clean we can build our app on top of it.
Please open docker documentation, that will come handy:
https://docs.docker.com/engine/reference/builder/



In the root directory "05-Dockerfile-and-building-an-image" create a new file called "Dockerfile" and on top of it we will add

```
FROM tiangolo/uwsgi-nginx-flask:python3.7
```
and then we move our app to the container. Read the documentation and please do so.
If you need any help please flag your benevolent dictators.


Then you can build your image with 
```
Docker build .
```

And then run your app, open the correct port and show the rest of the team the beautiful output of your app.
Bonus point if you can add a picture if you have the time to do so.
