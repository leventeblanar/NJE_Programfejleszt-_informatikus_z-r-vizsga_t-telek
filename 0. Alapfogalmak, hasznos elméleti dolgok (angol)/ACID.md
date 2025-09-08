<h2>ACID compliant database</h2>

- acronym (Atomicity, Consistency, Isolation, Durability)
- it describes the key properties oof a database transaction
- Atomicity :
    - a transaction is all-or-nothing
    - if a part of a transaction fails, the whole transaction is rolled back
    example: transferring money -> debit succeeds , credit fails, entire transaction is undone
- Consistency:
    - A transaction must leave the database in a valid state, following all rules, constraints and triggers
    - example: CHECK constraint: "balance can't go below 0" -> database won't let a transaction violate that rule
- Isolation:
    - transaction run independently of each other
    - example: booking for last place - only one goes through
- Durability:
    - once the transaction is commited the data is permanent, even if there's a crash or power failure
    - example: after you clikc pay in an online shop, the order is stored securely and won't vanish if the server restarts


<h2>Why is it important?</h2>

- prevets data corruption
- ensures reliable transactions
- maintains trust (users now that once they commit something, it's correct and stays that way)
- without ACID, databasases could lose money transfers, duplicate bookings or create inconsistent records

