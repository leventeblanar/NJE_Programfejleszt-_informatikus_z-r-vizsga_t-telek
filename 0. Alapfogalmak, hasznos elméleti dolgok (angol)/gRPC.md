<h2>gRPC - Google Remote Procedure call</h2>

- a high-performance, open-source RPC (Remote Procedure Call) framework
- allows programs to execute procedures on remote computers like local functions
- developers don't need to handle remote interaction details, and client/servers can use different programming languages
- built on top of HTTP/2
- Uses Protocol Buffers (Protobufs) as the default data serialization format

Instead of just sending JSON back and forth like in REST, gRPC generates code for you (stubs) in multiple langiages -> calling a function on another server feels almost like calling a local function on your own code 

<h4>Why is it special?</h4>

- super fast & efficient - HTTP/2 supports multiplexing, compression, binary framing. Protobuf is compact and faster to parse than JSON
- stringly typed contracts - service definied in a .proto file - both client and server generates code from this
- Cross-language support - write a server in Go, a client in Python, another in Java all talking to each other without manually writing parsers
- Streaming support - not just requests/response
    - Unary RPCs (normal request/response, like REST)
    - Server streaming (one request, multiple responses)
    - Client streaming (multiple requests, one response)
    - Bi-directional streaming (both send and receive stream like a chat app)
- Code generation - you don't write boilerplate for serialization/deserialization - protobuf complier (protoc) does that


<h4>When is gRPC used?</h4>
- internal microservices: servicies inside a large system need high performance and strong contracts
- low-latency systems: financial trading platforms, gaming backends
- loT/edge systems: where bandwidth is limited, protobuf is lighter than JSON
- real-time communication: voice, video, chat, telemetry


<h4>Real-life examples</h4>
- Google – Surprise, they use it everywhere internally. Gmail, Google Cloud APIs, etc. Many of Google Cloud’s APIs are gRPC under the hood.
- Netflix – Uses gRPC for internal service-to-service communication in their massive microservices ecosystem.
- Square (Cash App) – Uses gRPC to link backend microservices that handle payments and user data.
- Kubernetes – Uses gRPC for communication between components like the kubelet and API server.
- Spotify – Their backend services (like playlists, recommendations, streaming metadata) often talk over gRPC.