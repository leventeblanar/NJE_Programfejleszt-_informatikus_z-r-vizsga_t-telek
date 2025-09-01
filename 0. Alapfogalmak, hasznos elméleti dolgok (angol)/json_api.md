<h2>JSON APIs</h2>

JSON:API is a specification (not a separate API) that defines how servers and clients should structure and exchange data using JSON. Its main purpose is to standardize API responses, so developers don’t have to reinvent their own JSON formats for every project.

- is a specigfication/standard that defines how data should be sent and received in JSON
- goal: to create a consistent format for data exchange
- example: if you have a 'user' resource, JSON API says that the response should look like this?

```json
{
  "data": {
    "type": "users",
    "id": "1",
    "attributes": {
      "name": "Alice",
      "email": "alice@example.com"
    }
  }
}
```

- this is useful because every API following JSON API looks the same, making it easier to build client-side integrations.

KeyFeatures:
- Consistent format: Defines how resources, attributes, relationships, errors, pagination, and filtering should be represented in JSON.
- Interoperability: Any client that understands JSON:API can work with any server that implements it.
- Efficiency: Reduces the amount of data transferred by supporting sparse fieldsets, includes, and batching.