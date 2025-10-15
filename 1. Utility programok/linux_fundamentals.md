<h1>Linux Fundamentals</h1>

youtube: https://www.youtube.com/playlist?list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK

**Unix vs Linux**
I felt that I have to settle the difference here as this was my first question here as well. Unix was created in the 1970s and was a ommand-line operating system originally, but later it evolved to support graphical interfaces. It became popular in universities, enterprises and internet servers due to its reliability and multitasking capabilities.
The goal was to create an operating system that could communicate with different machines and support networking, especially for servers. 

While Unix was powerful, it's closed-source nature was limiting. Because of that Linus Torvalds - as a student - decided to build his own kernel for his final year project. By combining C and Assembly language he created a new kernel and called it Linux. The speciality of Linux was that it was open-source therefore anyone could view, modify and distribute it freely. Also, Linux could handle much more (computer hanrdware, software, hame development, mainframes).

**Why Linux?**
- tonns of services run on Linux
- enduser systems run on Linux
- many server, cloud, and DevOps tools, making it a vital skill in IT and software development
- it runs everywhere: servers, cloud, containers, CI/CD, embedded devices
- troubleshooting & control as if a service breaks, the CLI is how you fix it

**What counts as "fundamentals?**
- Shell usage: navigating (cd, ls), globs/quoting, pipes & redirects, job control.
- Filesystem & permissions: FHS layout, chmod/chown/umask, sudo.
- Processes & services: ps/top/htop, signals (kill), systemctl, logs (journalctl, /var/log).
- Packages: apt/dnf/pacman, adding repos, verifying installs.
- Networking: ip/ss, ping, curl, ports/firewalls basics.
- Text tools: grep, sed, awk, cut, sort, uniq, find, xargs.
- Users & env: users/groups, $PATH, env vars, dotfiles.
- Disks: df/du, mounts, fstab.
- Remote & scheduling: ssh/scp, cron or systemd timers.
- Editors: be comfortable in at least one (nano/vim).

