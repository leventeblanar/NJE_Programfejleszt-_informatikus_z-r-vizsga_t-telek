<h2>APIs</h2>

What is an API?
- Application Programming Interface
- an API is an interface for a client to communicate with a server
client: usually an outsider application (webbrowser, console app)
server: a computer that hosts the application, which can be a website, a database system or something else
- in practice: a client messages a server through a Web Request and the server processes the request and send a response
- the web requests: HTTP Request - uses the HTTP Protocol

The 4 most common types of HTTP requests are:
1. GET - retrieve data from the server - fetch info, no sideeffects on the server
2. POST - submit data to the server - create new resource 
3. PUT - Update a resource on the server 
4. DELETE - Request the removal of a resource on the server

Types of APIs:
1. Web APIs: apis that work over the internet (e.g.: REST API, GraphQL API)
2. Library APIs: Functions/methods that you can use in a programming language (like math.qrt() in Python) 
3. Operating System APIs: functions to interact with OS resources (files, memory, etc.)

What is a REST API?
- The REST API is a type of web API that uses HTTP methods like the above mentioned (GET, POST, PUT, DELETE)
- Uses URLs to represent resources
- often returns data in JSON format

What is CRUD?
C - Create - POST
R - Read - GET
U - Update - PUT
D - Delete - DELETE

Example with the Pokemon API:
1. Requesting a certain entry
```python
import requests

# Define the URL of the API endpoint
pokemon_name = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(f"Name: {data['name']}")
    print(f"Height: {data['height']}")
    print(f"Weight: {data['weight']}")
    print("Types:")
    for t in data['types']:
        print(f" - {t['type']['name']}")
else:
    print("Failed to retrieve data")
```

2. Sorting several entries
```python
url = "https://pokeapi.co/api/v2/pokemon?limit=5"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for p in data['results']:
        print(f"Pokémon name: {p['name']} - URL: {p['url']}")

```