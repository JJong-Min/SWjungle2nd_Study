class Person {
    constructor(name, first, second) {
        this.name = name;
        this.first = first;
        this.second = second;
    }
    sum() {
        return this.first + this.second;
    }
    
}

class PersonPlus extends Person{
    avg() {
        return (this.first + this.second) / 2;
    }
    
}

var kim = new Person('kim', 10, 20);
console.log("kim.sum()", kim.sum());

var lee = new PersonPlus('lee', 10, 20);
console.log("lee.sum()", lee.avg());