# AirBnB Clone - The Console

## Description
This is the first step of the AirBnB clone project. It consists of a
command interpreter (console) built in Python to manage AirBnB objects
such as User, State, City, Place, Amenity, and Review.

## The Command Interpreter
The console allows you to:
- Create new objects (ex: a new User or a new Place)
- Retrieve an object from a file (JSON)
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

### How to start it
Interactive mode:
$ ./console.py
(hbnb)

text

Non-interactive mode:
$ echo "help" | ./console.py
(hbnb)

text

### How to use it
(hbnb) create BaseModel
(hbnb) show BaseModel <id>
(hbnb) destroy BaseModel <id>
(hbnb) all
(hbnb) all BaseModel
(hbnb) update BaseModel <id> <attribute name> "<attribute value>"
(hbnb) quit

text

### Examples
.
/
c
o
n
s
o
l
e
.
p
y
(
h
b
n
b
)
c
r
e
a
t
e
U
s
e
r
49
f
a
f
f
9
a
−
6318
−
451
f
−
87
b
6
−
910505
c
55907
(
h
b
n
b
)
s
h
o
w
U
s
e
r
49
f
a
f
f
9
a
−
6318
−
451
f
−
87
b
6
−
910505
c
55907
[
U
s
e
r
]
(
49
f
a
f
f
9
a
−
6318
−
451
f
−
87
b
6
−
910505
c
55907
)
′
i
d
′
:
′
49
f
a
f
f
9
a
−
6318
−
451
f
−
87
b
6
−
910505
c
55907
′
,
.
.
.
(
h
b
n
b
)
u
p
d
a
t
e
U
s
e
r
49
f
a
f
f
9
a
−
6318
−
451
f
−
87
b
6
−
910505
c
55907
f
i
r
s
t
n
a
m
e
"
B
e
t
t
y
"
(
h
b
n
b
)
a
l
l
[
"
[
U
s
e
r
]
(
49
f
a
f
f
9
a
−
6318
−
451
f
−
87
b
6
−
910505
c
55907
)
′
f
i
r
s
t
n
a
m
e
′
:
′
B
e
t
t
y
′
,
.
.
.
"
]
(
h
b
n
b
)
d
e
s
t
r
o
y
U
s
e
r
49
f
a
f
f
9
a
−
6318
−
451
f
−
87
b
6
−
910505
c
55907
(
h
b
n
b
)
q
u
i
t
./console.py(hbnb)createUser49faff9a−6318−451f−87b6−910505c55907(hbnb)showUser49faff9a−6318−451f−87b6−910505c55907[User](49faff9a−6318−451f−87b6−910505c55907) 
′
 id 
′
 : 
′
 49faff9a−6318−451f−87b6−910505c55907 
′
 ,...(hbnb)updateUser49faff9a−6318−451f−87b6−910505c55907first 
n
​
 ame"Betty"(hbnb)all["[User](49faff9a−6318−451f−87b6−910505c55907) 
′
 first 
n
​
 ame 
′
 : 
′
 Betty 
′
 ,..."](hbnb)destroyUser49faff9a−6318−451f−87b6−910505c55907(hbnb)quit

text

## Files
- `models/` - all model classes
- `models/engine/file_storage.py` - serialization engine
- `console.py` - the command interpreter
- `tests/` - unit tests
