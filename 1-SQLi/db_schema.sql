drop table if exists prism_people;
create table prism_people (
  id integer primary key autoincrement,
  name text not null,
  secret text not null
);

insert into prism_people values (null, "Obama", "PRISM");
