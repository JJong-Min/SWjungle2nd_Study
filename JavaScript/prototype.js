function Person(name, first, second, third) {
    this.name = name;
    this.first = first;
    this.second = second;
}

// 이렇게 빼주면 객체가 만들어질 때마다 실행되는 것이 아닌 호출될 때 한번만 실행됨.
Person.prototype.sum = function() {
    return this.first + this.second;
}

var kim = new Person('kim', 10, 20);
var lee = new Person('lee', 10, 10);
console.log("kim.sum()", kim.sum());
console.log("lee.sum()", lee.sum());