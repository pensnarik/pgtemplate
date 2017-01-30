UPDATE pg_database SET datallowconn = 'false' WHERE datname = :'database_name';
SELECT pg_terminate_backend(pid) from pg_stat_activity where datname = :'database_name';
DROP DATABASE IF EXISTS :database_name;
