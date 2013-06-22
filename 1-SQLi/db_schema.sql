drop table if exists prism_secrets;
create table prism_secrets (
  id integer primary key autoincrement,
  name text not null,
  secret text not null
);

-- Insert random name/secret in the database
insert into prism_secrets values (null, "Obama", "PRISM");
insert into prism_secrets values (null, "George W Bush", "petroleum");
insert into prism_secrets values (null, "Angela Merkel", "We want our own prism");
insert into prism_secrets values (null, "Dingo", "not a dog");
insert into prism_secrets values (null, "Superman", "cry when he sees a green rock");
