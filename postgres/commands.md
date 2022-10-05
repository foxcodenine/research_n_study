    
### connecting

    sudo -i -u postgres

    psql

    <!-- ----------------------------------------------------------- -->

    \l                          # list databases;
    \c animals;                 # connect to animal db;
    \d+                          # display tables;
    \d cats;                    # discribe cats table;    

    <!-- ----------------------------------------------------------- -->

    create database animals;
    drop database animals;

    insert into cats (id, name, age) values (1, 'Lara', 6), (2, 'Tina', 12);

    <!-- ----------------------------------------------------------- -->


### dump data

    pg_dump  animals > animals_all.sql

    pg_dump -s            animals > animals_tables.sql
    pg_dump --schema-only animals > animals_tables.sql

    pg_dump -a            animals > animals_data.sql
    pg_dump --data-only   animals > animals_data.sql

    <!-- ----------------------------------------------------------- -->
### copy data as cvs 

    copy (select * from cats where id > 5) To '/tmp/cats.sql'

    <!-- ----------------------------------------------------------- -->

### Restoring (db should be create aheads)
    psql -d animals < animals_s.sql

    <!-- ----------------------------------------------------------- -->

### How to dump a partial/sample table in postgres using pg_dump

    CREATE TABLE cats_tmp AS ( SELECT * FROM cats WHERE id > 5);

    pg_dump animals --table cats_tmp | sed 's/public.cats_tmp/public.cats/' > /tmp/cats_partial.sql

    psql -d animals < /tmp/cats_partial.sql
