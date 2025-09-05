<h2>ORM - Object-Rational Mapping</h2>

- is a programming technique that allows developers to interact with a relational database using object-oriented programming concepts 
- ORM frameworks map database tables to cloasses and words to objects -> enables dev. to perform database operations through objects rather than raw sql queries
- simplifies data manipulation, improves code mantainability by aligning database interactions with the application's object model


Instead of doing this:
```sql
SELECT * FROM users WHERE id = 1;
```

You can do this:
```python
user = session.query(User).filter_by(id=1).first()
```

Behind the scenes, the ORM translates your python code into SQL and executes it on the database.

<h4>Where does it sit?</h4>
ORM is kind of in the middle of your code and the database.
- works with objects
- maps these objects to database tables
- handles the conversation between objects <-> rows


```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String)

# create and save to DB
new_user = User(name="Alice")
session.add(new_user)
session.commit()
```