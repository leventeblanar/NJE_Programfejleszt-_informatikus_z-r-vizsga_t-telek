<h2>GraphQL</h2>

GraphQL is a query language for APIs and a runtime for executing those queries against your data. Instead of multiple fixed REST endpoints, GraphQL lets clients ask exactly for the data they need in a single request—nothing more, nothing less.

**Why it’s important:**
- Efficiency – reduces over-fetching and under-fetching of data.
- Flexibility – clients control the shape of the response.
- Single endpoint – simplifies API structure compared to many REST endpoints.
- Strong typing – schemas define the data types and relationships clearly.
- Developer experience – built-in tools like introspection and documentation make APIs easier to explore and maintain.

In short: GraphQL streamlines communication between frontend and backend, improving performance and developer productivity.
Want me to also give you a quick GraphQL vs REST comparison so you see why companies switch?


**GrapQL vs. REST**
```
                            REST                                    GraphQL
==========================================================================================================================================
Endpoints                   Many                                    Single
Data Fetching               Fixed resp.                             client gets exactly what they need
                            can over and underfetch
Request struct.             URL+HTTP methods (Get,Post,Put,Del)     Queries&Mutations in a structured schema
Response shape              Determined by the server                determined by the client
Versioning                  often req. new version                  Schema envolves with deprication instead of breaking changes
Typing                      No strong typing (JSON)                 Strongly typed schema (types, relations, validation)
Tooling                     Limited auto-documentation              Introspection + tools like GraphiQl/Playground make exploring APIs easy
```