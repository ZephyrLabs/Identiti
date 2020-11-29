# Identiti

![Identiti Logo](Identiti.bmp "Identiti Logo")

##### Made by S.Sravan a.k.a "ZephyrLabs"

is a password manager made with _**Python**_ (Front-end) and _**MySQL**_ (Back-end)

_Checks:_
* published under _**GPLv3 license**_

#### What is Identiti ?
> Identiti is an open source Password manager that runs on Python and interfaces with MySQL, 
> its uses a basic terminal based UI interface to communicate with the user
> The project is a very simple concept of how a Password manager works...

Identiti has simple features such as,
* storing Password of a particular account
* has basic Caesar-cypher encryption
* has a failsafe mechanism for each function
* has logging capabilities
* has basic prevention from hackers and trespassers attempting malicious methods of data interception such as Injections etc.

I hope to further expand the project to become a password managing server for one's computer, 
and allows one to locally access and manage their passphrases..

The Project still has future outlook for things like Encrypted storage, physical Authentication keys, etc.

#### What do you need to run Identiti ?
>You will require these basic requirements to Run Identiti
> * CPU running at a minimum of 400MHz
> * 256 MB of Free Memory
> * have Python 
> python 3.x [ >3.6.5],  and MySQL 8.x Installed, and operational

additionally with these things you will need to run some queries in MySQL to finish the setup

you can manually execute these queries in MySQL to finalise the setup,
 
```
create database db;
use db;
create table bst(username varchar(32) primary key, main_pass varchar(32) not null);
create table lut(username varchar(32) not null, user_account varchar(64) not null, user_pass varchar(32) not null);
```

> note: Auto setup will occur if it doesn't exist but it will require the user to create a database called 'db', 
>this can also be done via the psTerm (more info below)

with all of this set, you can go ahead and run the main program to start the service, Enjoy! :)

##### note: 
>please run the program with 
> ``` python3 gui.py ```
>in the system console (cmd, linux terminal etc.)


## Basic Manual of Identiti
#### Main Menu
The Main menu of Identiti gives options for one to,
* login,
* learn more about the software ( brings you here :) )
* and close the program

within the login you can,
* create a new account ,and
* login to your existent account

once you login,
* fetch your password
* add a password
* update a password
* delete a password ,and
* delete your account

within the App typing 'exit' while in a menu will let you go back to the outer menu

#### psTerm
psTerm, 
is the internal emulated terminal console for MySQL within Python
this is for testing, debugging and maintenance purposes

its is only accessible by giving the MASTER_AUTH_KEY as you option in the main menu

psTerm mostly accepts all standard MySQL queries, along with a few extra additions 

```clear```
will clear the console window

```exit```
will exit the console window ,and bring one back to the main screen

```reset```
will reset the entire database

```about```
will give a shorthand manual about psTerm and how to use it, 

psTerm is not a fully fledged sql terminal, rather its use extends in the field of debugging and internal access
to the database and tables during program runtime, rather than needing a separate terminal
