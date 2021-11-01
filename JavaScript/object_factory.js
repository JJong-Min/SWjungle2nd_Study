var kim = {
    name: 'kim',
    first: 10, 
    second: 20,
    third: 30,
    sum: function() {
        return this.first + this.second + this.third;
    }
}

var lee = {
    name: 'kim',
    first: 10, 
    second: 20,
    third: 10,
    sum: function() {
        return this.first + this.second + this.third;
    }
}
console.log(kim.sum());
console.log(lee.sum());

// 객체를 찍어내는 공장 만들기 (Constructor)
var d1 = new Date('2021-11-01');
console.log(d1.getFullYear());

function Person(name, first, second, third) {
    this.name = name;
    this.first = first;
    this.second = second;
    this.third = third;
    this.sum = function() {
        return this.first + this.second + this.third;
    }
}

var kim = new Person('kim', 10, 20, 30);
console.log(kim.sum());
