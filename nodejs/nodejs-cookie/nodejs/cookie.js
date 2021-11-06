var http = require('http');
var cookie = require('cookie');

http.createServer(function(request, response){
    // parse는 undifined를 만나면 고장남(예외처리)
    var cookies = {};
    if (request.headers.cookie !== undefined) {
        cookies = cookie.parse(request.headers.cookie);
    }
    
    response.writeHead(200, {
        'Set-Cookie': ['yummy_cookie=choco', 'tasty_cookie=strawberry']
    })
    response.end('Cookie!!');
}).listen(3000); 