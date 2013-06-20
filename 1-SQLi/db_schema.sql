drop table if exists prism_secrets;
create table prism_secrets (
  id integer primary key autoincrement,
  name text not null,
  secret text not null
);

insert into prism_secrets values (null, "Obama", "PRISM");
