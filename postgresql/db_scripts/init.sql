create table data(
  id serial primary key,
  email text not null,
  date text not null
);

insert into data(email, date)
values('test1@mail.ru', '01.01.2021 01:01:01');

insert into data(email, date)
values('test2@gmail.com', '02.02.2022 02:02:02');

insert into data(email, date)
values('test3@mailbox.it', '03.03.2023 03:03:03');
