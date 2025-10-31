<h2>Docker tutorial by Mosh Hamedani</h2>

Since I have already scripted the basics in a different file, I will just skip these at this point.

1. **Virtual machines vs. Containers**
Container: isolated environment for running an application
Virtual Machines (VM): An abstraction of a machine (physical hardware)

The problems with a virtual machine:
- Each VM needs a full-blown OS
- Slow to start
- Resource intensive
- given memory of given pc needs to be distributed between the pc and the vm 

Containers:
- Allow running multiple apps in isolation
- lightweight
- use OS of the host
- start quickly
- needs less hardware resources

2. **Docker Architecture**
- Client server architecture (client component that talks to the server component through a rest API. [server -> Docker Engine])
- all the containers share the OS of the host, therefore share the kernel of the host (Kernel - is the core of on OS, it manages applications and hardware resources)

3. **Development Workflow**
- Application to be dockerised needs a Dockerfile -> this includes everything that needs to be in the Docker Image
- Image contains:
    - A cut-down OS
    - A runtime environment (eg Node)
    - Application files
    - Third-party libraries
    - Environment variables
- Once we have an image -> start -> gets loaded inside a container


4. **Docker in Action**
1st step:
    I created the app.js file, with a simple print statement
2nd step:
    To have this as a docker container we have to respect the order of the statements in our Dockerfile as follows:
        - Start with an OS
        - Install Node
        - Copy app files
        - Run node app.js
3rd step:
    After writing the entire dockerfile build it: docker build -t hello-docker .
4th step:
    Check existing images: docker image ls
    Check existing containers: docker container ps -a
5th step:
    Run the docker file: docker run hello-docker 


6. **Chosing the correct Linux-distribution for your docker image**
- Linux has several different distribution versions (Ubuntu, Debian, Alpine, etc...)
- I will have to research this later tho...........................................

7. **Working with Docker - Ubuntu**
- docker run ubuntu (this will pull and run an image with ubuntu)
- docker ps -a : check currently available images
- docker run -it ubuntu (-it is the interactive mode where the terminal will host a shell to pass commands to the kernel&

8. **Package manager**
- apt (Advanced Package Tool)

Continue: https://www.youtube.com/watch?v=pTFZFxd4hOI