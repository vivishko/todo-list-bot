# docker postgres

this is a note for myself, but maybe it will be useful for you too <br>
here is some commands that i use to manage my postgres container <br><br><br>
___

#### docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' some-postgres

! replace some-postgres with the name of your container </br>
\* this will give you the IP address of the container </br>

#### docker exec some-postgres psql -U postgres -l 

! replace like in previous one </br>
! replace postgres with your username </br>
\* this will give you a list of databases </br>

#### docker exec some-postgres psql -U postgres -d todo_bot_db -c "\dt+"

! replace like in previous one </br>
! replace todo_bot_db with your database name </br>
\* this will give you a list of tables in your database </br>

#### docker exec some-postgres psql -U postgres -d todo_bot_db -c "drop table public.todo"

! replace like in previous one </br>
! replace todo with your table name </br>
\* this will drop the table todo </br>
you will need to do this if you want to change the table structure </br>

#### docker exec some-postgres psql -U postgres -d todo_bot_db -c "table public.user"
or 
#### docker exec some-postgres psql -U postgres -d todo_bot_db -c "select * from public.user"
! replace like in previous one </br>
\* this will give you data of this table </br>