<h2>REST API</h2>

REST API (Representational State Transfer Application Programming Interface) is an architectural style for desginging networked applications. It relies on standard HTTP methods (GET, POST, PUT, DELETE)to interact with resources, which are represented as URIs (Uniform Resource Identifiers).

Stateless:
- no state is stored on the server
- every request is independent and contains all the necessary info (auth token, parameters)
- the server doesn't remember what you did before or whether you're logged in
- if you send the same request again 10 minutes later, the server responds the same way, because all the info is inside the request

    Pros:
    - Easier to scale (any server can handle the request, no session needed)
    - simpler architecture
    - matches the REST philosophy better

    Cons:
    - you need to send authentication/identification info in every request

Stateful:
- the server remembers the state (session, user login status)
- first req: client logs in -> server creates a session
- subsequent requests don't need to send all info again - server keeps track of who you are

    Pros:
    - less data needs to be passed with each request
    - convenient for certain use cases (classic web apps, shopping cart)

    Cons:
    - Harder to scale (reqiests must go to the same server - or sessions must be replicated)
    - more complex fault tolerance (if one server dies, the session can be lost)


<h4>SWAGGER use with Python (FAST API)</h4>

Rest API in Python is FAST API. It is a restless API but Swagger stores the authentication information and pastes it into the requests automatically every time. 