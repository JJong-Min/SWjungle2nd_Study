var http = require('http');
var fs = require('fs');
var url = require('url');

var app = http.createServer(function(request,response){
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;

    console.log(url.parse(_url, true));
    if (pathname === '/') {
      fs.readFile(`data/${queryData.id}`, 'utf-8', function(err, description){
        var title = queryData.id;
        if (queryData.id === undefined) {
          var title = 'Welcome';
          var description = 'Hello, Node.js';
        }
        fs.readdir('./data', function(error, filelist){
          var list = `<ul>`;
          var i = 0;
          while(i < filelist.length) {
            list += `<li> <a href="/?id=${filelist[i]}"> ${filelist[i]}</a> </li>`;
            i += 1;  
          }
          list += `</ul>`
          var template = `
          <!doctype html>
          <html>
          <head>
            <title>WEB1 - ${title}</title>
            <meta charset="utf-8">
          </head>
          <body>
            <h1><a href="/">WEB</a></h1>
            ${list}
            <h2>${title}</h2>
            <p>${description}</p>
          </body>
          </html>
          `;   
          response.writeHead(200);
          response.end(template);
        })
      });
  } else {
    response.writeHead(404);
    response.end('Not Found');
  }
});
app.listen(3000);