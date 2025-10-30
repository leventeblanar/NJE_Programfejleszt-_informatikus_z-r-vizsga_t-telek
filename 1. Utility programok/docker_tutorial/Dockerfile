FROM node:alpine

# . means all the files and /app means the destination
COPY . /app 

# if we use WORKDIR we do not need to specify a relative path for the CMD command, it could be simply app.js but if not /app/app.js
WORKDIR /app

# execute command
CMD node app.js


# docker build -t hello-docker .
# here the . means the current directory, meaning we have to be in the directory where the Dockerfile is