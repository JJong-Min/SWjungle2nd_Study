class Person {
    constructor(name, first, second) {
        this.name = name;
        this.first = first;
        this.second = second;
    }
}

Person.prototype.sum = function() {
    return this.first + this.second;
}

var kim = new Person('kim', 10, 20);
console.log('kim', kim);
console.log("kim.sum()", kim.sum());