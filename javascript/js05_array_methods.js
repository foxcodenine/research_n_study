const ppp = i => console.log(`\n(${i})______________________________________\n`)

ppp('A')// _____________________________________________________________________
// Array.form()

// The Array.from() method creates a new, shallow-copied Array instance from an
// array-like or iterable object.

console.log(Array.from('foo'));
// [ 'f', 'o', 'o' ]


// Syntax:   Array.from(arrayLike [, mapFn [, thisArg]])

/*
arrayLike:          An array-like or iterable object to convert to an array.

mapFn Optional:     Map function to call on every element of the array.

thisArg Optional    Value to use as this when executing mapFn.
*/

ppp('B')// _____________________________________________________________________

let chris = 'Christopher';
let chrisX2 = Array.from(chris, i => i.repeat(2)).join('');

console.log(chrisX2);

ppp('C')// _____________________________________________________________________

// Array from a set:

const set = new Set(['foo', 'bar', 'baz', 'foo']);
console.log(Array.from(set));

ppp('D')// _____________________________________________________________________

// Array from a Map:

const map = new Map([[1, 2], [2, 4], [4, 8]]);

console.log(map);
console.log(Array.from(map));

const mapper = new Map([['1', 'a'], ['2', 'b']]);

console.log(Array.from(mapper.values()));
console.log(Array.from(mapper.keys()));
