# AirBnB_clone
ALX AirBnB Clone Project

## Description
This is the very first of four different phases in an attempt to replicate the AirBnB web-based application. In this first part of the project, an elementary console was set up using the Cmd Python module to control all of the project's objects. This facilitated the implementation of the create, show, update, all, and destroy methods to the classes and subclasses which were already in effect.

## Environment
This console is developed using Ubuntu 23.10 using version 3.12.3 of Python 3.

## Usage of the Console

### How to Install the Console
To install the console, simply run the command:
```
$ git clone https://github.com/MutaiT/AirBnB_clone.git

```
### How to Use the Console
The table below lists the commands used to operate the console and what they all do:

| Command | 					Function                                                |                        
|-------- | --------------------------------------------------------------------------------------------|
| show    | Outputs an instance's string representation depending on its id and class name.             |
| all     | Outputs every instance's string representation, whether or not the class name is specified. |
| create  | Creates an object of a given class.                                                         |
| count   | Finds out how many instances of a class there are.                                          |
| update  | Adds or modifies attributes to an instance, updating it according to the class name and id. |
| destroy | Deletes an instance by using its id and class name.                                         |
| help    | Prints out what a specific command does.                                                    |
| quit    | Exit the program.                                                                           |

#### Example 1:
```
(hbnb) create User
4bfe50ff-747c-4062-8c98-2da9405b84c1
(hbnb) show User 4bfe50ff-747c-4062-8c98-2da9405b84c1
[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018)}
(hbnb) all User
["[User] (597beedb-5d39-4546-a4d5-f3ddf2ae7d82) {'id': '597beedb-5d39-4546-a4d5-f3ddf2ae7d82', 'created_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 757687), 'updated_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 759466), 'first_name': 'John', 'age': '69'}", "[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018)}"]
(hbnb) update User update 4bfe50ff-747c-4062-8c98-2da9405b84c1 name Betty
** no instance found **
(hbnb) update User update 4bfe50ff-747c-4062-8c98-2da9405b84c1 name Betty
** no instance found **
(hbnb) update User 4bfe50ff-747c-4062-8c98-2da9405b84c1 name Betty
(hbnb) all User
["[User] (597beedb-5d39-4546-a4d5-f3ddf2ae7d82) {'id': '597beedb-5d39-4546-a4d5-f3ddf2ae7d82', 'created_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 757687), 'updated_at': datetime.datetime(2023, 7, 16, 11, 10, 55, 759466), 'first_name': 'John', 'age': '69'}", "[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018), 'name': 'Betty'}"]
(hbnb) destroy User 597beedb-5d39-4546-a4d5-f3ddf2ae7d82
(hbnb) all
["[User] (4bfe50ff-747c-4062-8c98-2da9405b84c1) {'id': '4bfe50ff-747c-4062-8c98-2da9405b84c1', 'created_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 99815), 'updated_at': datetime.datetime(2023, 7, 16, 16, 50, 53, 101018), 'name': 'Betty'}"]
(hbnb) show User 597beedb-5d39-4546-a4d5-f3ddf2ae7d82
** no instance found **

```
