

'https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance'

console.log(`_________________________________Prototypal inheritance__________________________________`);

console.log('A','_______________________________________________________________________________________')
//Getting started

function Person(first, last, age, gender, interests) {
   
    this.name = {first, last};
    this.age = age;
    this.gender = gender; 
    this.interests = interests;    
};

Person.prototype.greeting = function() {
    alert('Hi! I\'m ' + this.name.first + '.');
};

console.log(Person);

var chris = new Person('Chris', 'Farrugia', 35, 'male', 'programming');
console.log(chris);
chris.greeting();

console.log('B','_______________________________________________________________________________________')



// Defining a Teacher() constructor function

// createing Teacher by inheriting from Person with call()
function Teacher(first, last, age, gender, interests, subject) {
    Person.call(this,first, last, age, gender, interests);
    this.subject =subject;
};


Teacher.prototype = Object.create(Person.prototype); // <-- to inherit methods on Person()'s prototype. 
                                                     //  however this has set the teacher properties to person
console.log(Teacher.prototype.constructor); 


// this will reset the properties back to teacher

Object.defineProperty(Teacher.prototype, 'constructor', { 
    value: Teacher, 
    enumerable: false, // so that it does not appear in 'for in' loop
    writable: true });

console.log(Teacher.prototype.constructor);



console.log('D','_______________________________________________________________________________________')



var vanessa = new Teacher('Vanessa', 'Mintof', 40, 'female', 'drawing', 'maths');

console.log(vanessa);
vanessa.greeting();



console.log('E','_______________________________________________________________________________________')

//Inheriting from a constructor with no parameters 

function Brick() {
    this.width = 10;
    this.height = 20;
}


function BlueGlassBrick() {
    Brick.call(this);
    
    this.opacity = 0.5;
    this.color = 'blue';
}


var blueSquare = new BlueGlassBrick();

console.log(blueSquare);


console.log('F','_______________________________________________________________________________________')


//Giving Teacther() a new prototype function goodmorning()

Teacher.prototype.goodmorning = function() {
    let prefix;
    
    if(this.gender === 'male' || this.gender === 'Male' || 
       this.gender === 'M'    || this.gender === 'm') {
        prefix = 'Mr.';
    } else if (this.gender === 'female' || this.gender === 'Female' ||
               this.gender === 'F'      || this.gender === 'f') {
        prefix = 'Ms.';
    } else {
        prefix = 'Mx.';
    }
    
    alert(`Good morning, my name is ${prefix}${this.name.last} and I'm your ${this.subject} teacher.`)
}

vanessa.goodmorning();



console.log(`_____________________________________Object.create()_____________________________________`);

'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create'

//The Object.create() method creates a new object, using an existing object as the prototype of the newly created object.

const dummy = {
    isHuman: false,
    printIntro: function() {
        console.log(`My name is ${this.name}. Am I human? ${this.isHuman}`)
    }
};

const matthew = Object.create(dummy);
matthew.name = 'Matthew';
matthew.isHuman = true; //<- overwrite inherite property

matthew.printIntro();



`Syntax   Object.create(proto, [propertiesObject])`

const james = Object.create(dummy, {name: {value:'James'}, isHuman: {value: true}})


console.log('G','_______________________________________________________________________________________')


// inherite from a prototype object with  __proto__   ref: Speaking JavaScript page213

var AnimalProto = {
    
    kingdom: 'animal',
    
    printDesc: function() {
        console.log(`${this.name} is a ${this._class} in the family of ${this.family}.`)
    }
};


var fox = {
    __proto__: AnimalProto,
    _class: 'mammal',
    family:'Canidae',
    name : 'fox'
};

console.log(fox);

fox.printDesc();
console.log(fox.kingdom);
console.log(fox.__proto__);

















