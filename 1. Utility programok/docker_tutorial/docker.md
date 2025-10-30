<h2>Docker</h2>

**The process of creating a docker file and running a a docker image**

**The docker file**
1. Create Dockerfile in the root folder of the project
2. Elements:
    ADD	- Add local or remote files and directories.
    ARG	- Use build-time variables.
    CMD	- Specify default commands.
    COPY - Copy files and directories.
    ENTRYPOINT - Specify default executable.
    ENV - Set environment variables.
    EXPOSE - Describe which ports your application is listening on.
    FROM - Create a new build stage from a base image.
    HEALTHCHECK - Check a container's health on startup.
    LABEL - Add metadata to an image.
    MAINTAINER - Specify the author of an image.
    ONBUILD - Specify instructions for when the image is used in a build.
    RUN - Execute build commands.
    SHELL - Set the default shell of an image.
    STOPSIGNAL - Specify the system call signal for exiting a container.
    USER - Set user and group ID.
    VOLUME - Create volume mounts.
    WORKDIR - Change working directory.


    


3. How to build and run your image:
    - docker buiild -t (name tag) username/imagename
    - docker run 


Example: 
```
# 1. BASE IMAGE - always start with this
FROM node:18-alpine

# 2. WORKdirectory - copy everything here
WORKDIR /app

# 3. DEPENDENCY COPY - (FIRST!)
# Why first? Docker caches layers
# If the code changes but the dependencies do not, you do not have to reinstall
COPY package*.json ./

# 4. dependency install
RUN npm ci --only=production

# 5. COPY CODE
COPY . .

# 6. BUILD (if needed)
RUN npm run build

# 7. PORT declare (documentation)
EXPOSE 3000

# 8. USER (for security reasons don't run as root)
USER node

# 9. START COMMAND
CMD ["node", "dist/index.js"]
```

**Tags**
```
docker run \
  --rm \                    # Auto-delete after stop
  -d \                      # Detached mode (background)
  --name my-container \     # Name the container (easier to reference)
  -p 8080:3000 \           # Port forward (host:container)
  -e KEY=value \           # Single ENV variable
  --env-file .env \        # Load ENV variables from file
  -v $(pwd)/data:/data \   # Volume mount (data persistence)
  --network my-net \       # Specify network
  --restart unless-stopped \ # Auto-restart policy
  --memory="512m" \        # Memory limit
  --cpus="1.5" \          # CPU limit
  -it \                    # Interactive terminal (needed for bash)
  myimage:latest \         # Image name
  /bin/bash                # Override command (optional)
```


