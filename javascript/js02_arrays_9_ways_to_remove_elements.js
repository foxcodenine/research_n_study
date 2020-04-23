const pline = function(i) {
    console.log(`\n(${i})___________________________________________\n`)};




pline('A'); // _________________________________________________________    

// 1. Removing Elements from End of a JavaScript Array

// Setting the length property to a value less than the current value.
// Any element whose index is greater than or equal to the new length
// will be removed.

`.length`

let a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

console.log(a.length);

a.length = 5;
console.log(a);

a.length = 10;
console.log(a);



pline('B'); // _________________________________________________________ 

// The pop method removes the last element of the array, returns that element,
// and updates the length property.

`.pop()`

let b = ['A', 'B', 'C', 'D', 'E', 'F', 'F', 'G', 'H', 'I'];

let c = b.pop()

console.log(b);
console.log(c);

pline('C'); // _________________________________________________________ 

// Removing Elements from Beginning of a JavaScript Array


let d = ['zero', 'one', 'two', 'three'];
let e = d.shift();

console.log(d);
console.log(e);


pline('D'); // _________________________________________________________ 

// Using Splice to Remove Array Elements
'.splice(start, howmany, item1toBeAdded, ..., itemXtoBeAdded)'

let f = ['A', 'B', 'C', 'D', 'E', 'F', 'F', 'G', 'H', 'I'];
let g = f.splice(2,4);

console.log(f);
console.log(g);

pline('E'); // _________________________________________________________ 

// Removing Array Items By Value Using Splice

let h = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 5, 9, 0];

for( let i = 0; i < h.length; i++){
    if ( h[i] === 5) {
        h.splice(i, 1); 
    }
}
console.log(h);

// As the items are removed from the array the index still increments and the
// next item after your matched value is skipped.

pline('F'); // _________________________________________________________ 


// The simple solution is to modify the above example to decrement the index
// variable so it does not skip the next item in the array.
let j = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 5, 9, 0];
for( let i = 0; i < j.length; i++) {
    if ( j[i] === 5) {
        j.splice(i, 1); 
        i--; 
    }
}
console.log(j);

pline('G'); // _________________________________________________________ 

// The Lodash Array Remove Method 

`filter`

// Unlike the splice method, filter creates a new array. filter() does not
// mutate the array on which it is called, but returns a new array. 

let k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];

let m = k.filter(function(value, index, arr)
    { return value > 5;});

console.log(m);

pline('H'); // _________________________________________________________ 

let n = k.filter(function(value, index, arr)
    { return value !== 5;});


console.log(n);

pline('i'); // _________________________________________________________ 

// Making a Remove Method

let t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];


function arrayRemove(arr, value) {
    return arr.filter(function(ele){
        return ele != value;
    });
}
var result = arrayRemove(t, 6);

console.log(result);

pline('i'); // _________________________________________________________ 

// Explicitly Remove Array Elements Using the Delete Operator
`delete`

// The delete operator does not affect the length property. Nor does it affect
// the indexes of subsequent elements. The array becomes sparse, the deleted
// item is not removed but becomes undefined

let o = [1, 2, 3, 4, 5, 6];
delete o[4]; 
console.log(o);


pline('J'); // _________________________________________________________ 

// Clear or Reset a JavaScript Array

let p = [1, 2, 3, 4, 5, 6];

// The references to this variable will still hold the original array's values
let q = p; 

p = [];

console.log(p);
console.log(q);

let r = [1, 2, 3, 4, 5, 6];

let s = r; 


// A simple trick to clear an array is to set its length property to 0
r.length = 0;

console.log(r);
console.log(s);

pline('K'); // _________________________________________________________ 



