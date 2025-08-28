<h2>Authentication</h2>

API authentication is the process of verifying the identity of clients attempting to access an API, ensuring that only authorized users or applications can interact with the API's resources.

Common methods:
- API keys
- OAuth 2.0
- JSON Web Tokens (JWT)
- basic authentication
- OpenID Connect


<h4>JWT</h4>

JSON Web Token is an open standard for securely transmitting information between parties as a JSON object.

Consists of 3 parts: 
1. header (specifies token type and algorithm used for signing)
2. payload (contains the claims or the data being transmitted)
3. signature (which is used to verify the token's integrity and authentication)

Compact, self-contained and can be easily transmitted in HTTP headers, making them popular for modern web and mobile applications.

<h4>OAuth</h4>

Open standard for authorization that allows third-party applications to access a user's resurces without exposing their credentials.
It works by issuing access tokens after users grant permission, which applications then use to interact with resource servers on behalf of the user.

The process involves:
- a resource owner (the user)
- a resource server (which holds the data)
- authorization server (which issues the token)

Enables secure, token-based access management, commonly used for granting applications perfmissions to interact with services like social media accounts or cloud storage. 

<h4>Basic Authentication</h4>

Simple HTTP authentication scheme built into the HTTP protocol. 
Process: sending the user's credentials encodied in base64 format within the HTTP header.
Client makes a request -> server response: 401 status code and a "WWW-Authenticate" header -> Client resend request (with authhorization header and "Basic" followed by the base64-encoded username, pw)

Important:
- significant security limitations
- cred is basicly decodeable with base64 
- doesn't provide any encryption

Should only be used through HTTPS connections -> cred protected during transmission

<h4>Token authentication</h4>

Token-based authentication is a protocol which allows users to verify their identity and in return receive a unique access token.
During the life of the token users can access the website or app that the token has been issued for - no need to reenter information.
However if the user logs out or quits the app the token is invalidated.

Tokens offer a second layer of security and administrators have detailed control over each action and transaction.

<h4>Cookie-Based Authentication</h4>

Cokkie-based authentication is a method of maintanining user sessions in web applications. When a user logs in, the server creates a session and sends a unique identifier (session ID) to the client as a cokkie. This cookie is then sent with every subsequent request, allowing the server to identify and authenticate the user. 

Actual session data -> stored on server -> cookie merely serving as a key
This method is stateful on the server side and works well for traditional web applications.
Easy to implement, natively supported by browsers. 

issues:
- challenges with cross-origin requests
- can be vulnerable to CSRF attacks if not properly secured
- may not be ideal for modern single-page applications or mobile apps

<h4></h4>