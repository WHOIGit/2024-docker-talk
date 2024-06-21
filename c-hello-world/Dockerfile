# start with a base image containing the GCC compiler
FROM gcc

# copy the source code to the image
COPY hello-world.c /usr/src/hello-world.c

# set the working directory to /usr/src
WORKDIR /usr/src

# perform the compilation, creating an executable named hello-world
RUN gcc -o hello-world hello-world.c

# set the default command to run the executable when the container starts
CMD ./hello-world