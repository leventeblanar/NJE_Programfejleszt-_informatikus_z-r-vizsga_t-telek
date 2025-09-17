<h2>Kernel</h2>

What is a Kernel?
- it is a bridge between 'userspace' and hardwares
- it is not an operating system - instead it is a program layer

A kernel is THE program that the operating system runs, everything else is run on top of the kernel. How? Usually all the stuff you run on your computer is run as a program, and the kernel provides what this program needs to run.

An operating system's main job is to run programs and the kernel is the code that actually runs to allow this to happen. Kernels create little sandboxes (this is the technical term btw) for programs to play in and give them all the tools they need to do whatever. The kernel hands over control of the CPU to all the processes so they can run the code they run then yanks it away so that something else can run, it provides RAM as needed so that the program has scratch paper to run, whenever the program has to access a file it asks the kernel to fetch it for it, anytime you press your keyboard or click your mouse the kernel tells the program that the keyboard/mouse was clicked. If a program has nothing to do at this current moment it just gives back the CPU to the kernel so that it can do whatever/hand it over to what needs it next.