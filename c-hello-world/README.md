# "Hello, world" in C

This section covers how to create and deploy an executable in a Docker image.

To do this, the following things need to be done at build time:

* Provision a C compiler
* Copy the source code into the image
* Compile the code
* Create a command to run the code

## First implementation

The simplest implementation is to start with a base image containing a compiler. In this case we'll use `gcc`, which is available on Docker Hub.

```
FROM gcc
```

Now we need to copy the source code from the host OS to the running build container. We'll copy it to `/usr/src`.

```
COPY ./hello-world.c /usr/src/hello-world.c
```

Now we'll change our working directory in the build container to `/usr/src`. This allows us to use paths relative to that directory.

```
WORKDIR /usr/src
```

Next, we'll compile the executable.

```
RUN gcc -o hello-world hello-world.c
```

Finally, we'll set the image's initial command to run the executable.

```
CMD ./hello-world
```

### Issues with this implementation

* Built on a large base image (>1GB) containing gcc and all of its dependencies
* Executable is small, resulting image is large

We can fix this with multistage builds.

## Second implementation with multistage build

```
# start with a base image containing the GCC compiler
FROM gcc AS builder

# copy the source code to the image
COPY hello-world.c /usr/src/hello-world.c

# set the working directory to /usr/src
WORKDIR /usr/src

# perform the compilation, creating an executable named hello-world
RUN gcc -static -o hello-world hello-world.c

# now start with a base image containing only the executable
FROM scratch

# copy the executable from the builder image to the new image
COPY --from=builder /usr/src/hello-world /hello-world

# set the default command to run when the container starts
CMD ["/hello-world"]
```