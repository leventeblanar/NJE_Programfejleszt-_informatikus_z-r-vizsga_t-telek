<h2>Database Migration</h2>

- at their core, database migration is a form of version control for the database schema
- help track and manage changes to the structure of your database

**Why is it important?**
- Evolving Application Requirements: application grows -> more data storage needs, need to add new features, modify existing ones, optimize performance, all of them might require changes to your database shema 
- Collaboration: in a team environment, multiple developers might be working on different features that require database changes. Migration is a standard and organized way for everyone to apply these changes without these changes interfering with each other
- Consiistency Accross Environments: multiple envirponments for application (development, testing, staging, production), migrations ensure that your database schema is consistent across all these environments
- Reproducibility: migrations allow you to easily recreate your database schema from scratch,which is crucial for setting up new development enviroments, running tests, or reovering from disasters
- Rollback capability: allows you to undo changes. Important if you introduce a vreaking change or discover a bug

**Key concepts**
- Migration files: heart of the system: each migration typically contains the following:
    - Up (or Change) Method - the code that applies the changes
    - Down (or Revert) Method - the code that reverses changes made by the "up" method
- Migration Tool/Framework: This is the software that helps you create, apply, manage migrations
    - Rails Migrations (Roby on Rails): tightly integrated with the Rails framework
    - Flyway: A standalone migration tool that supports many databases (PostgreSQL, MySQL, ...)
    - Liquibase: Another popular standalone migration tool with a focus on flexibility
    - Alembic (Python/SQLAlchemy): designed to use with the SQLAlchemy ORM
    - Entitiy FrameWork Migrations (.NET): integrated with the Entitity Framework ORM
- Migration History(or schema version table): The migration tool keeps track of which migrations have been applied to the database