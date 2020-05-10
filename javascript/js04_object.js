console.log('A','_______________________________________________________________________________________')


// Object() constructor

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/Object



let oo = new Object();
oo.foo = 42;

console.log(oo);


console.log('B','_______________________________________________________________________________________')

// Object.assign() The Object.assign() method copies all enumerable own
// properties from one or more source objects to a target object. It
// returns the target object

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign


const target = {a: 1, b: 2};
const source = {b: 4, c: 5};

const returnedTarget = Object.assign(target, source);
console.log(target);
console.log(returnedTarget);

console.log('C','_______________________________________________________________________________________')


// Deep Clone:
const dd = oo ; 
oo.foo = 45;

console.log(dd);
console.log(oo);

// Shallow Copy:

const ss = Object.assign({}, oo);
oo.foo = 46;

console.log(oo);
console.log(ss);

console.log('D','_______________________________________________________________________________________')

// Merging objects

const o1 = {a: 1};
const o2 = {b: 2};
const o3 = {c: 3};

Object.assign(o1, o2, o3);
console.log(o1);


const o4 = {d: 4, e: 4, f: 4};
const o5 = {e: 5, f: 5};
const o6 = {f:6 }
Object.assign(o4, o5, o6);
console.log(o4);

console.log('E','_______________________________________________________________________________________')

// Object.entries() 

// Object.entries() method returns an array of a given object's own
// enumerable string-keyed property [key, value] pairs

chris = new Object({name:'Chris', surname: 'Farrugia', age: 35});
console.log(chris);

chrisArray = Object.entries(chris);
console.log(chrisArray);  // [ 'name', 'Chris' ], [ 'surname', 'Farrugia' ], [ 'age', 35 ] ]


// Using for  of loop:

for (let [key, value] of Object.entries(chris)){
    console.log(`${key} >> ${value}`)
};


// Converting an Object to a Map:

const dorothy = {firstName: 'Dorothy', lastName: 'Cassar', city: 'Qormi'};

const dorothyMap = new Map(Object.entries(dorothy));
console.log(dorothyMap);


// Iterating through an Object: 

Object.entries(dorothy).forEach(([k, v]) => console.log(`${k}, ${v}`))


console.log('F','_______________________________________________________________________________________')

// Object.keys() & Object.values()


dorothyKeys = Object.keys(dorothy);
console.log(dorothyKeys);

dorothyValues = Object.values(dorothy);
console.log(dorothyValues);




console.log('G','_______________________________________________________________________________________')

// Object destructuring

const user = {
    id: 166,
    role: 'admin',
    is_verified: true
}

const {id, role, is_verified} = user;

console.log(id);
console.log(role);
console.log(is_verified);

// Assignment without declaration 

const {name, spice} = {name: 'Ben', spice: 'mouse'};

console.log(name);
console.log(spice);

// Assigning to new variable names 


const bird = {variety: 'Canary', color: 'Yellow'};

const {variety: genus, color: hue} = bird;

console.log(genus);
console.log(hue);


console.log('H','_______________________________________________________________________________________')

// Object.freeze() and Object.seal()

Object.freeze(bird);

bird.color = 'Red';
console.log(bird);

delete bird.color;
console.log(bird);




const fish = {variety: 'Tuna', color: 'GrayBlue'};

Object.seal(fish);

fish.variety = 'Salmon'; fish.color = 'Pink';
delete fish.color;
console.log(fish);

console.log('i','_______________________________________________________________________________________')

// Object.preventExtensions()

const insect = {
    variety: 'Spider', 
    genus: 'Tarantula'
};

insect.legs = 8;
Object.preventExtensions(insect);
insect.eyes = 8;
console.log(insect);

console.log('j','_______________________________________________________________________________________')

// Object.isSealed() , Object.isFrozen() and Object.isExtensible()

// bird, fish, insect 

myObject = {bird:bird, fish:fish, insect:insect}


// Object.isSealed()

funcIsSealed = (obj) => {   
    arr = Object.entries(obj);

    for(let i of arr){
        console.log(`${i[0]} is Sealed: ${Object.isSealed(i[1])}`)
    };   
}

funcIsSealed(myObject);

console.log('______________________')



// Object.isFrozen() 

funcIsFrozen = (obj) => {   
    arr = Object.entries(obj);

    for(let i of arr){
        console.log(`${i[0]} is Frozen: ${Object.isFrozen(i[1])}`)
    };   
}

funcIsFrozen(myObject);



// Object.isExtensible()

console.log('______________________')

funcIsExtensible = (obj) => {   
    arr = Object.entries(obj);

    for(let i of arr){
        console.log(`${i[0]} is Extensible: ${Object.isExtensible(i[1])}`)
    };   
}

funcIsExtensible(myObject);


console.log('k','_______________________________________________________________________________________')

// try, catch, finally , throw



// https://www.w3schools.com/js/js_errors.asp
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch
// https://www.w3schools.com/jsref/jsref_try_catch.asp

const object1 = {};

Object.preventExtensions(object1);

try {
  Object.defineProperty(object1, 'property1', {
    value: 42
  });
} catch (e) {
  console.log(e);
}

console.log('to_continue.......')