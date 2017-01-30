# pgtemplate

pgtemplate is a wrapper for official PostgreSQL Dockerfile which allows you to create your
databases in container easily. pgtemplate provides the option of passing arguments from
external environment to SQL scripts.

## Example docker-compose.yml

The only mandatory argument is a name of a database. You should prefix variable with `INSTALL_`
to pass it inside the container. Variable which stores database name is called `INSTALL_DATABASE_NAME`.

```
version: '2'

networks:
  database:

services:
  database:
    image: database
    environment:
      PG_LOG_MIN_MESSAGES: 'info'
      PG_LOG_MIN_DURATION_STATEMENT: '0'
      INSTALL_DATABASE_NAME: test
    cpuset: 0,1
    mem_limit: 512M
    networks:
      - database
    ports:
      - '20000:5432'
```


To start container with provided empty database just run:

    $ docker build . -t database && docker-compose rm -f database && docker-compose up database


## Tuning postgresq.conf

Currenlty you can change the values of these variables:

Variable | Default value | Docker variable
---------|---------------|------------
max_wal_senders | 60 | PG_MAX_WAL_SENDERS
max_connections | 150 | PG_MAX_CONNECTION
log_min_duration_statement | 0 | PG_LOG_MIN_DURATION_STATEMENTS
log_min_messages | warning | PG_LOG_MIN_MESSAGES
synchronous_commit | off | PG_SYNCHRONOUS_COMMIT
