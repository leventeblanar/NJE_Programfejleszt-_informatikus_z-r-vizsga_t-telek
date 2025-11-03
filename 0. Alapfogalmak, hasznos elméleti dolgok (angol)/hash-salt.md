<h2>HASH - SALT</h2>

**HASH**
- a one-way mathematical function that transforms an input (e.g., password) into a fixed-length, random-looking string
- the password cannot be reversed/decoded from it
- the same password always produces the same hash
- no matter how long the password is, the hash is always the same length

**What is Salt?**

**Salt** is a **randomly generated string** that is added to the password **before hashing**.

**Problem without salt:**
```
User1 password: "macska123" → hash: "abc123def..."
User2 password: "macska123" → hash: "abc123def..."  ← THE SAME!
```

If two users use the same password, they get the same hash. → **Rainbow table attack** is possible!

**Solution with salt:**
```
User1: "macska123" + salt("xK9p2") → hash: "abc123def..."
User2: "macska123" + salt("mQ7r8") → hash: "zyx987uvw..."  ← DIFFERENT!
```