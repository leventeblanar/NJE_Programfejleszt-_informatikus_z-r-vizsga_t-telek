<h2>Data Synchronization</h2>

Definiation: keeping data consistent and up to date across multiple locations - such as tables, databases, services or even files.
Whenever data in one place changes, those changes need to be reflected elsewhere to avoid mismatches or stale info.

<h3>Common Data SyncSchenarios</h3>

- Table-to-table sync in the same database
    - Example: You have a products table and a stock_levels table.
    - You want to ensure that when a product is deleted from products, it’s also removed from stock_levels.

- Snyc between staging and production databases
    - Example: After verifying updates in a test (staging) environment, you push them to production – you need to sync the data.

- Sync between systems (e.g. CRM - ERP)
    - A customer is updated in Salesforce → That change should be reflected in your internal Postgres DB too.

<h3>How to do data sync?</h3>

1. Triggers (within a DB)
```SQL
CREATE TRIGGER delete_stock_after_product
AFTER DELETE ON products
FOR EACH ROW
DELETE FROM stock_levels WHERE product_id = OLD.id;
```


2. ETL Scripts / Sync Scripts (Python example)
```python
import psycopg2

def sync_users():
    conn1 = psycopg2.connect("dbname=db1 ...")
    conn2 = psycopg2.connect("dbname=db2 ...")

    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()

    # Get users from db1
    cursor1.execute("SELECT id, name FROM users WHERE synced = false;")
    new_users = cursor1.fetchall()

    # Insert into db2
    for user in new_users:
        cursor2.execute("INSERT INTO users (id, name) VALUES (%s, %s)", user)

    # Mark as synced
    for user in new_users:
        cursor1.execute("UPDATE users SET synced = true WHERE id = %s", (user[0],))

    conn1.commit()
    conn2.commit()
```

3. Scheduled Syncs (e.g., with cron, Airflow, Task Scheduler)
- This is a basic method of using certain appliences that lets you run a script X minutes/hours/days. Simple and reliable

4. Change Data Capture (CDC)
- This is a pro technique used in data pipelines.
- You "listen for changes in a database (inserts, updates, deletes) and propagate them elsewhere in real time
 
**Tools**
- Debezium
- Kafka Conenct
- PostgreSql logical replication
- EventBridge / AWS DMS

5. Checksum-based sync
Compare records by hash/checksum:
- SELECT md5(concat(col1, col2)) FROM table ...
- Compare checksums across systems → Only sync if they differ
