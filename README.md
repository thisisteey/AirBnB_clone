# 0x00. AirBnB clone - The console

## 0x00.Table of contents

* [0x01 Introduction](#0x01-Introduction)
* [0x02 Installation](#0x03-Installation)
* [0x03 Testing](#0x04-Testing)
* [0x04 Usage](#0x04-Usage)
* [0x05 Authors](#0x05-Authors)

## 0x01 Introduction

Team project to build a clone of [AirBnB](https://www.airbnb.com/).

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project visit the [Wiki](https://github.com/ralexrivero/AirBnB_clone/wiki).

The console will perform the following tasks:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### Storage

All the classes are handled by the `Storage` engine in the `FileStorage` Class.

## 0x02 Installation

```bash
git clone https://github.com/aysuarex/AirBnB_clone.git
```

change to the `AirBnb` directory and run the command:

```bash
 ./console.py
```

### Execution

In interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

in Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## 0x03 Testing

All the test are defined in the `tests` folder.

### Python Unit Tests

* unittest module
* File extension ``` .py ```
* Files and folders star with ```test_```
* Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
* Execution command: ```python3 -m unittest discover tests```
* or: ```python3 -m unittest tests/test_models/test_base.py```

### run test in interactive mode

```bash
echo "python3 -m unittest discover tests" | bash
```

### run test in non-interactive mode

To run the tests in non-interactive mode, and discover all the test, you can use the command:

```bash
python3 -m unittest discover tests
```

## 0x05 Usage

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

### Commands

> The commands are displayed in the following format *Command / usage / example with output*

* Create

> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*

```bash
create <class>

```

```bash
(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
```

* Show

```bash
show <class> <id>
```

```bash
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```

* Destroy

> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*

```bash
(hbnb) create User
0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) destroy User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) show User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
** no instance found **
(hbnb)
```

* all

> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) create BaseModel
e45ddda9-eb80-4858-99a9-226d4f08a629
(hbnb) all BaseModel
["[BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) [BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) {'id': '4c8f7ebc-257f-4ed1-b26b-e7aace459897', 'created_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447155), 'updated_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447257), 'name': 'My First Model', 'my_number': 89}"]
["[BaseMode
```

* count

> *Prints the number of instances of a given class.*

```bash
(hbnb) create City
4e01c33e-2564-42c2-b61c-17e512898bad
(hbnb) create City
e952b772-80a5-41e9-b728-6bc4dc5c21b4
(hbnb) count City
2
(hbnb)
```

* update

> *Updates an instance based on the class name, id, and kwargs passed.*
> *Update the file.json*


## Authors
<details>
    <summary>FARUQ OLAMIDE SOKUNBI</summary>
    <summary>TAIWO ADEOYE DADA</summary>
</details>

## How to add Author file
`Bash script for generating the list of authors in git repo`

```bash
#!/bin/sh

git shortlog -se \
  | perl -spe 's/^\s+\d+\s+//' \
  | sed -e '/^CommitSyncScript.*$/d' \
  > AUTHORS
```
