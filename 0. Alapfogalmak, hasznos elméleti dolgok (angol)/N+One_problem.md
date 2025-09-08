<h2>N + 1 problem</h2>

The N+1 problem occurs in database querying when an application perform a query to retrieve a list of items and then issues additional queries to fetch related data for each item individually. 
This often results in inefficiencies and performance issues because the number f queries issued grows proportionally with the number of queries  issued grows proportionally with the number of items retrieved. 

Example: 
-   application retrieves 10 items -> additional query for each item
-   results in 11 queries insted of 2 (1 for the list, 10 for the details)
-   severely impact performance, instead with larger datasets 

Solution:
-   optimizing queries to use joins or batching techniques to retrieve related data in fwer more efficient queries
