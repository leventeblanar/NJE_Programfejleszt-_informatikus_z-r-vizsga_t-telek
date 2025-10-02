<h2>Web servers</h2>

Web servers handle client requests and serve web content like HTML pages and images. Process HTTP/HTTPS requests, interact with databases, and send responses. Popular servers include Apache, Nginx and IIs. Essential for hosting websites, managing traffic, and providing SSL/TLS security.

**short:**
- it is a computer that hosts web pages, making them accessible online

A webserver does:
1. listens
2. on a port
3. for a request
4. sent via a transport protocol
5. sends a response
6. containing the requested resource

**Main duties:**
- stores and delivers files to browsers, making your site accessible to users
- processes files for emails and data storage using SMTP, FTP

**Main components:**
- Software: The web server software controls how users access hosted files. It comprises several components and houses at least an HTTP server to process and respond to incoming requests.
- Hardware: It stores web server software and its files, such as static HTML documents, JavaScript files, and CSS stylesheets. The web server hardware also connects to the internet, enabling data exchange with other physical devices.


<h4>The process of communication:</h4>
1. to load a website, the browser will look for the web server hosting the site's files
2. To achive this, the web broser translates the site's domain name into an IP address via the Domain Name System (DNS) -> cache if frequently used
3. After finding the corresponding web server, the browser sends an HTTP request to retreve site content
4. Web server receives and processes the HTTP request through its HTTP server - HTTP server accepts request, it will search through the database to obtain relevant data
5. the server returns the files to the web browser and delivers them to users


**Two main types:**
1. Static: consists only a computer and HTTP sftware
2. Dynamic: static web server plus extra software (application server, databases)



<h4>Web servers in the market</h4>
- Apache HTTP Server. A free and open-source web server used for many operating systems, including Windows, Linux, and macOS. Apache is one of the most popular choices among website owners, developers, and hosting providers, with a market share of over 31%.

- NGINX. Initially designed only for HTTP web serving, this open-source software now also serves as a reverse proxy, HTTP load balancer, and email proxy. NGINX is known for its speed and ability to handle multiple connections, making it suitable for high-traffic websites.

- Microsoft Internet Information Services (IIS). A closed web server software developed by Microsoft, IIS is widely used in Windows operating systems. It supports Active Server Pages (ASP), a server-side scripting technology developed by Microsoft for creating dynamic and interactive web applications.

- Lighttpd. A free and open-source web server software known for its fast data processing with less CPU power. Lighttpd is also popular for its small memory footprint, allowing the server to handle more requests while maintaining responsiveness and performance.


<h2>NGINX</h2>

<h4>HTTP Web Server</h4>

- the most basic function
- browser send an HTTP request to a web server -> pl. GET /index.html
- for example: nginx in this case is the webserver that returns the HTML, CSS, Images or whatever the webpage needs

<h4>Reverse Proxy</h4>
- does not directly connect to the webserver but to NGINX
- NGINX takes over the request and forwards it to a different server (eg. Python/Node.js app)
- it's like a receptionist taking over your call and deciding where to forward it

<h4>Content Cache</h4>
- NGINX is able to store frequently used content (eg. pictures, HTML, API responses)
- next time it does not request the server, but gets it from the cache

<h4>Load Balancer</h4>
- if you have more than 1 server NGINX will divide the requests between them
- eg.: you have 3 servers but all the users go to the same example.com -> nginx slits the requests so not all of them goes to the same location so they are not overloaded
- it can be round robin, or intelligent load balancing

<h4>TCP/UDP Proxy server</h4>
- NGINX is not only good for HHTP, but can handle several protocols
- TCP: eg. database conn
- UDP: eg. cideo stream, DNS request, game servers
It can stream, hide or load balance as well on these too

<h4>Mail Proxy server</h4>
- nginx can handle e-mail protocols as well (IMAP, POP3, SMTP)
- its not the transport layer but proxy
- you have more email servers, nginx will handle these properly and forward accordingly
- you can use it as authentication layer as well


```
             🌍 Internet / Böngésző
                     |
                     v
        ┌───────────────────────────┐
        │          NGINX            │
        │  - Reverse Proxy          │
        │  - Cache (CSS/IMG/JS)     │
        │  - Load Balancer          │
        └─────────┬───────────────┘
                  |
    ┌─────────────┴─────────────────┐
    v                               v
┌───────────────┐           ┌───────────────┐
│  WebApp #1    │           │  WebApp #2    │
│ (pl. FastAPI) │           │ (pl. FastAPI) │
└───────────────┘           └───────────────┘

```