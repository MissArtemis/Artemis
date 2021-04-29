use mr_artemis;
show tables;
create table user_info (
    id int auto_increment primary key ,
    user_name varchar(255) not null,
    password varchar(255) not null ,
    email varchar(255) not null,
    phone varchar(255) not null
)