## Open Redis

    $ redis-cli
<hr>
## Redis Commands 


    > PING 
    PONG

    > ECHO hello
    hello 

##### SET and GET

    > SET foo 100 
    > GET foo 
    100 

##### Increase and Decrease
    > INCE foo
    101

    > INCEBY foo 10 
    111

    > DECR foo 
    110 

    > DECR foo 10 
    100

##### Check if Exist and Delete
    > EXISTS foo
    (integer) 1

    > EXISTS bar
    (integer) 0

    > DEL foo
    > EXISTS foo
    (integer) 0

<hr>

#### Close Redis 

    ctrl+c

#### Redis from the Terminal 

    $ redis-cli echo 'hello redis world!'
    "hello redis world!"

#### More Commands 

##### Delete all key value pairs 

    > FLASHALL

####
    > SET server:port 8000 
    > SET server:name red_block

##### EXPIRE
    > SET firstName james
    > EXPIRE firstName 120 
    > TTL firstName 
    (integer) 97

    # after 120 seconds

    > TTL firstName
    (integer) -2

    > SET lastName cassar 
    > TTL lastName 
    (integer) -1


##### MSET
    > MSET key1 "val1" key2 "val2"


##### MSETNX 
    > MSET key1 "val1" key2 "val2"
    OK

    > MSET key3 "val3" key2 "val2"
    (integer) 0 

* NX commands -- Only set the key if it does not already exist.
* XX commands -- Only set the key if it already exist.

##### SETNX (If the key already exists, it will not change)
    > SETNX animal fox
    (integer) 1

    > SETNX animal cat
    (integer) 0


##### RENAME and RENAMENX

    > RENAME name fullname
    OK

    > GET fullname
    "christopher"

    > RENAMENX key1 fullname
    (integer) 0

##### MGET 
    > MGET key1 key2
    1) "val1"
    2) "val2"

##### APPEND 
    > APPEND key2 _value2
    > get key2
    "val2_value2"

##### GETRANGE 
    > SET name christopher 
    > GETRANGE name 4 -1
    "stopher"

##### GETSET (will get old value and set it to new value)
    > SET name christopher
    OK

    > GETSET name james
    "christopher"

##### SETEX (same as set and expire)
    > SETEX surname 120 manduca
    OK

    > TTL surname
    (integer) 102

##### PSETEX (same as SETEX but in milliseconds)
    > PSETEX SURNAME 120000 cassar

##### PTTL (same as TTL but in milliseconds)
    > PTTL SURNAME 
    (integer) 103554

##### PERSIST (remove the timeout on a key)

    > PTTL surname
    (integer) 41023

    > PERSIST surname
    (integer) 1
    
    > pttl surname
    (integer) -1

<hr>
#### SCAN
##### (SCAN iterates the set of keys in the database, return only a small amount per call)

    > scan 0
    1) "5"
    2)  1) "surname"
        2) "name"
        3) "key6"
        4) "key50"
        5) "key1"
        6) "key3"
        7) "key30"
        8) "key60"
        9) "key2"
    10) "key10"
    11) "key5"

    > scan 5
    1) "0"
    2) 1) "animal"
    2) "key40"
    3) "key20"
    4) "key4"

##### SCAN COUNT 

    > SCAN 0 COUNT 4
    1) "12"
    2) 1) "surname"
    2) "name"
    3) "key6"
    4) "key50"

    > SCAN 12 COUNT 3
    1) "14"
    2) 1) "key1"
    2) "key3"
    3) "key30"

##### SCAN MATCH

    > SCAN 0 MATCH key10
    1) "5"
    2) 1) "key10"

    > SCAN 0 MATCH key*
    1) "5"
    2) 1) "key6"
    2) "key50"
    3) "key1"
    4) "key3"
    5) "key30"
    6) "key60"
    7) "key2"
    8) "key10"
    9) "key5"

#### SCAN with other data types:

> SSCAN

> HSCAN

> ZSCAN

<hr>

### KEY Pattern
 
Supported glob-style patterns:

    h?llo matches hello, hallo and hxllo

    h*llo matches hllo and heeeello

    h[ae]llo matches hello and hallo, but not hillo

    h[^e]llo matches hallo, hbllo, ... but not hello

    h[a-b]llo matches hallo and hbllo

Use \ to escape special characters if you want to match them verbatim.


    > KEYS *name*
    1) "surname"
    2) "name"

##### RANDOMKEY (Return a random key from the database)

    > RANDOMKEY
    "key10"

<hr>

## Client & Config

##### CONFIG GET

Used to read tge configuration parameters of a running Redis server.
Takes sigle arguments.

    > CONFIG GET port
    1) "port"
    2) "6379"

    # Gets the port configuration value.

    > CONFIG GET *

    # List all support config params.

##### CONFIG SET 
    CONFIG SET configoption "newvalue"
    
    # Used to reconfigure server at runtime without haveing to do a restart.


##### INFO
    # The INFO command returns information and statistics about the server.

    > INFO
    > INFO server 

Options: 
* server
* client
* memory
* stats 
* cpu  
* all 
* persistence 
* commandstats
* cluster 
* keyspace 
* default
    
##### CCONFIG RESETSTAT    
Resets the statistics reported by Redis using the INFO command.

    These are the counters that are reset:

    Keyspace hits
    Keyspace misses
    Number of commands processed
    Number of connections received
    Number of expired keys
    Number of rejected connections
    Latest fork(2) time
    The aof_delayed_fsync counter


#### COMMAND
Returns Array reply of details about all Redis commands.

    command name
    command arity specification
    nested Array reply of command flags
    position of first key in argument list
    position of last key in argument list
    step count for locating repeating keys

#### COMMAND INFO 
Returns detail for a spacifiv command 

    > COMMAND INFO GET
    1)  1) "get"
        2) (integer) 2
        3) 1) readonly
        2) fast
        4) (integer) 1
        5) (integer) 1
        6) (integer) 1

#### COMMAND COUNT
Returns Integer reply of number of total commands in this Redis server.

    > COMMAND COUNT
    (integer) 205

<hr>

#### CLIENT LIST
Returns info and stats on the clients connected to a server

    > CLIENT LIST
    id=3 addr=127.0.0.1:33936 fd=8 name= age=2406 idle=0 flags=N db=0 sub=0 psub=0 
    multi=-1 qbuf=26 qbuf-free=32742 obl=0 oll=0 omem=0 events=r cmd=client


#### CLIENT SETNAME
Assigns a name to a current client connection 
Displayed inthe output of CLIENT LIST

    > CLIENT SETNAME clientname

#### CLIENT GETNAME 
Returns the name of the current client connection
null reply if no name is set 

    > CLIENT SETNAME dorothy 
    > CLIENT GETNAME
    "dorothy"

#### CLIENT KILL
Closes up a given connection
Can use address/port or ID 

    > CLIENT KILL 127.0.0.1:portnum
    > CLIENT KILL id

<hr>

## Data Types

> https://redis.io/topics/data-types

* Strings 
* Lists 
* Sets 
* Hashes 
* Sorted sets

#### LIST
Redis Lists are simply lists of strings, sorted by insertion order. It is possible to add elements to a Redis List pushing new elements on the head (on the left) or on the tail (on the right) of the list.


 <b>LPUSH</b> command inserts a new element on the head.
 <b>RPUSH</b> inserts a new element on the tail.
 <b>LRANGE</b> returns specified elements of the list
 <b>LRANGE</b> returns specified elements of the list
 <b>LLEN</b> return the length of the list
 <b>LPOP</b> removes and return the first element of a list 
 <b>RPOP</b> removes and return the last element of a list
 

    > LPUSH friends Shawn
    (integer) 1

    > LPUSH friends Jose
    (integer) 2

    > RPUSH friends Eric
    (integer) 3

    > LRANGE friends 0 -1
    1) "Jose"
    2) "Shawn"
    3) "Eric"

    > LLEN friends
    (integer) 3

    > RPOP friends
    "Eric"

    > LPOP friends
    "Jose"
    
    > LRANGE friends 0 -1
    1) "Shawn"

#### SETS
* Sets are an unordered collection of Strings.
* It is possible to add, remove, and test for existence of members.
* Redis Sets have the desirable property of not allowing repeated members.
* Sets support a number of server side commands to compute sets.


 <b>SADD</b> Add one or more members to a set.
 <b>SREM</b> Remove one or more members from a set.
 <b>SMEMBERS</b> Remove one or more members from a set.
 <b>SISMEMBER</b> Tests if the given value is in the set.
 <b>SCARD</b> Return the count of members.



    
    > SADD carmarks subaru
    (integer) 1

    > SADD carmarks toyota
    (integer) 1

    > SADD carmarks honda
    (integer) 1

    > SMEMBERS carmarks
    1) "subaru"
    2) "honda"
    3) "toyota"

    > SREM carmarks subaru
    (integer) 1

    > SMEMBERS carmarks
    1) "honda"
    2) "toyota"

    > SISMEMBER carmarks toyota
    (integer) 1

    > SCARD carmarks
    (integer) 2

 <b>SMOVE</b> Moves member from one set to another.
 <b>SUNION</b> Combines two or more sets and returns a list of members.


    > SADD carmarks austin
    (integer) 1

    > SMOVE carmarks truckmarks austin
    (integer) 1

    > SUNION carmarks truckmarks 
    1) "austin"
    2) "toyota"
    3) "honda"

 <b>SDIFF</b> Return the members of the set resulting from the difference between the first and all successive sets.

    > SADD truckmarks toyota 
    (integer) 1


    > SMEMBERS truckmarks
    1) "austin"
    2) "toyota"

    > SMEMBERS carmarks
    1) "honda"
    2) "toyota"

    > SDIFF truckmarks carmarks
    1) "austin"
    > SDIFF carmarks truckmarks
    1) "honda"



    > SADD carmarks honda ford subaru toyota fiat jeep
    (integer) 0

    > SMEMBERS carmarks
    1) "jeep"
    2) "ford"
    3) "toyota"
    4) "fiat"
    5) "subaru"
    6) "honda"

    
    > SRANDMEMBER carmarks
    "honda"
    
    > SRANDMEMBER carmarks 3
    1) "ford"
    2) "fiat"
    3) "subaru"

<b>SPOP</b> Remove and retuns a random member from a specified set.

    
    > SPOP carmarks
    "ford"
    
    > SPOP carmarks 3
    1) "subaru"
    2) "fiat"
    3) "honda"














    









 








    



