console.log(new Date());
console.log(new Date().toLocaleString("en-US", {timeZone: "Asia/Seoul"}));
console.log(new Date(new Date().toLocaleString("en-US", {timeZone: "Asia/Seoul"})));