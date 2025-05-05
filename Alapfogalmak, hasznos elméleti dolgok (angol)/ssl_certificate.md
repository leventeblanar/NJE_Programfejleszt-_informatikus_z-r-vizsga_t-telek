<h2>SSL Certification</h2>

SSL (Secure Sockets Layer)
- A cryptographic protocol that secures communication between a client (like a browser) and a server.
- Its goal is to encrypt the data transmission, preventing third parties from eavesdropping (e.g., on passwords or sensitive data).

TLS (Transport Layer Security)
- TLS is the more secure, modern successor to SSL.
- TLS is what's actually used today (e.g., TLS 1.3), but people often still refer to "SSL certificates" out of habit.

**Summary:**
SSL = old protocol
TLS = its secure, updated replacement

An SSL certificate is a digital certificate issued by a trusted organization called a Certificate Authority (CA).

SSL certificates are what enable websites to use HTTPS, which is more secure then HHTP.
An SSL certificate is a data file hosted in a website's origin server. SSL certificates make SSL/TLS encryption possible, and they contain the website's public key and the website's identity, along with related information.


**SSL certificates include the following information in a single data file:**

- The domain name that the certificate was issued for
- Which person, organization, or device it was issued to
- Which certificate authority issued it
- The certificate authority's digital signature
- Associated subdomains
- Issue date of the certificate
- Expiration date of the certificate
- The public key (the private key is kept secret)



**How do SSL certificates and TLS work together?**

1. The server sends its certificate to the client.
2. The client (browser) verifies the certificate (e.g., is it signed by a trusted CA?).
3. Then, a TLS session is initiated, which:
4. Negotiates encryption keys
5. Starts encrypted communication
6. Ensures confidentiality and integrity of data


**Example**
- Browser -> https://webshop.hu
- server sends back its SSL certificate
- browser checks it and starts a TLS handshake (Transport Layer Security)
- data is transmitted through TLS securely