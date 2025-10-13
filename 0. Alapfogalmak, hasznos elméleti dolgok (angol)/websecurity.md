<h2>WebSecurity basics</h2>

**Web security** is the discipline focused on protecting web systems (web apps, APIs, browser interactions, and their supporting infrastructure) to ensure **confidentiality, integrity, and availability**.

* **Purpose:** safeguard data and functionality from unauthorized access, tampering, and outages.
* **Scope:** client (browser), network (TLS/HTTPS), server/app logic, databases, dependencies, and CI/CD.
* **Principles:** least privilege, secure defaults, input validation & output encoding, secure secrets management.
* **Common risks:** OWASP Top 10 (e.g., injection, XSS, broken access control, CSRF, SSRF).
* **Key controls:** strong authn/authz, parameterized queries, CSP & security headers, CORS, rate limiting, logging/monitoring.
* **Methodology:** build into the SDLC—SAST/SCA/DAST, code reviews, timely patching, and incident response.

In short: web security isn’t a single tool but a **set of practices, patterns, and checks** applied end-to-end—from design through operation.


<h4>How HTTP Works</h4>

What is HTTP protocol?
- the way websites work, servers, machines communicate
- application protocol
- works on the basis of request-response model (over TCP/IP)

TCP/IP protocol:
- transport layer protocol
- netcat shows us in bash how tcp protocol works
(if you use it in bash you have to write the HTTP message as well by hand: GET /index.php HTTP1.1 + Host: 127.0.0.1)

UDP protocol:
- works on one-way model
- it doesn't check if the data is sent but it just fires data packages to the end point
- 
