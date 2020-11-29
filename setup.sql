create database if not exists db;
use db;
create table if not exists bst(username varchar(32) primary key, main_pass varchar(32) not null);
create table if not exists lut(username varchar(32) not null, user_account varchar(64) not null, user_pass varchar(32) not null);