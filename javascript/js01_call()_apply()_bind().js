// https://tylermcginnis.com/this-keyword-call-apply-bind-javascript/


/*
call, apply and bind.
________________________________________________________________________

Whith call(), an object can use a method belonging to another object. It takes
'this value' and arguments provided individually.

Syntax: func.call([thisArg, arg1, arg2, ...argN])

    thisArg Optional
    The value to use as this when calling func

    arg1, arg2, ...argN Optional
    Arguments for the function.

________________________________________________________________________

The apply() method is similar to the call() method

    The difference is:

    The call() method takes arguments separately.

    The apply() method takes arguments as an array.



Syntax: func.apply(thisArg, [ argsArray])


Example: Math.max.apply(null, [1,2,3]); // Will also return 3

________________________________________________________________________



.bind is the exact same as .call but instead of immediately invoking 
the function, it’ll return a new function that you can invoke at a 
later time

let boundFunc = func.bind(thisArg, arg1, arg2, ...argN)



*/

// call:



var myPerson = {
    sayFullname: function() {
        console.log(this.name + ' ' + this.surname)    
    }
};


var chris = {
    name: 'Chris',
    surname: 'Farrugia',
    yearOfBirth: 1984
};

myPerson.sayFullname.call(chris)

// ________________________________________

// The call() method can accept arguments:

var myPerson2 = {
    calAge: function(year) {
        console.log(year - this.yearOfBirth);   
    }
};

var dorothy = {
    name: 'Dorothy', 
    surname: 'Cassar',
    yearOfBirth: 1990,    
}


myPerson2.calAge.call(dorothy, 2020);

// ________________________________________

// The call() without 'this'

var myGreetings = {
    goodmorning: function(name) {
        return'Good morning ' + name + '!';
    },

    goodnight: function(name) {
        return 'Good night ' + name + '!';
    },
}



var myString = myGreetings.goodnight.call(null,'Tania')
console.log(myString);

// _____________________________________________________________________

// apply:

myShape = {
    perimeter : function() {
        perimeter = 0
        
        for (var  i = 0; i < arguments.length; i++) {
            perimeter += arguments[i];
        }
        return perimeter
    }
};


myTrapezoid = [160, 400, 200, 350];

myTrapPerimeter = myShape.perimeter.apply(null, myTrapezoid);

console.log(myTrapPerimeter);



// _____________________________________________________________________

// bind:

var myPolygon = {
    calArea: function(){

        var perimeter, apothem, n, s;

        n = this.sides;
        s = this.sideLength   
        


        // 1. Calculate the perimeter
        perimeter = s * n;
      

        // 2. Determine the apothem
        var b = (Math.PI) / n 
        apothem = s / (Math.tan(b) * 2);
   

        // 3. Calculate the Area
        this.area = (perimeter * apothem) / 2     
    }   
};

var mySquare = {
    name: 'square',
    sides: 4,
    sideLength: 100
};

var myTriangle = {
    name: 'triangle',
    sides: 3,
    sideLength: 100
};

var myhexagon = {
    name: 'hexagon',
    sides: 6,
    sideLength: 100
};


myTriangle.calArea =  myPolygon.calArea.bind(myTriangle);
myTriangle.calArea();
console.log(myTriangle);

mySquare.calArea =  myPolygon.calArea.bind(mySquare);
mySquare.calArea();
console.log(mySquare);

myhexagon.calArea =  myPolygon.calArea.bind(myhexagon);
myhexagon.calArea();
console.log(myhexagon);



