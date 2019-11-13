## Ports and Volume with Docker

So the smart ones, should now have a remark !

We cannot access our nice postgres container and actually use it.


So we should forward the port to another port

```
sudo docker run -d -p 5432:5432 --name my-ov-postgres postgres
```

Where we specify that the port 5432 of the container is published on the port 5432 of my computer

We can now directly connect to the postgres using the psql command.

```
psql -h localhost -U postgres -d postgres
```


And we are connected to the psql prompt.

### Creating a table

As we are connected on the postgres console, we will create a table. 

```
postgres=# CREATE TABLE mytable (identifier INT, value VARCHAR);
```

We can now list the table in the postgres table :

```
postgres=# \dt
```

which will return the following lines :

```
          List of relations
 Schema |  Name   | Type  |  Owner   
--------+---------+-------+----------
 public | mytable | table | postgres
(1 row)
```

Let's quit the psql prompt with 

```
postgres=# \q
```

And let's kill our postgres container

```
sudo docker kill my-ov-postgres
```

let's restart it with the same docker run command than previously and list the tables we have in the database.
You should be able to get correct commands for that


**What is the problem ?**

### Using Volumes

As we have seen previously, the data is not persisted when we killed the container (or if he crash). Which is king of a problem.

There is something called volume that allow to "mount" the  

