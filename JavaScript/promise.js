'use strict';

// promise is a javascript object fro asynchronous operation.
// state: pending -> fulfilled or rejected
// producer vs consumer

// 1. producer
// when new promise is created, the executor runs automatically.
const promise = new Promise((resolve, reject) => {
    // doing some heavy work()
    console.log('doing something ...');
    setTimeout(() => {
        //resolve('ellie');
        reject(new Error('no network'));
    }, 2000);
});

// 2. Consumers: then, catch, finnaly
promise
    .then(value => {
        console.log(vlaue);
})
.catch(error => {
    console.log(error);
})
.finally(() => {
    console.log('finally');
})

// 3. Promise chaining
const fetchNumber = new Promise((resolve, reject)=> {
    setTimeout(() => resolve(1), 1000);
});
